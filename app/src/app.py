# Kivy dependencies
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# Other dependencies
import cv2
import tensorflow as tf
from layers import Dist
import os
import numpy as np


# App layout
class CamApp(App):

    def build(self):
        # Main layout
        self.web_cam = Image(size_hint = (1, .8))
        self.button = Button(text = 'Verify', on_press = self.verify, size_hint = (1, 0.1))
        self.verification_label = Label(text = 'Verification Uninitiated', size_hint = (1, 0.1))

        # Add items to layout
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)

        # Load keras model
        self.model = tf.keras.models.load_model('../model/siamesemodel.keras', custom_objects = {'Dist': Dist})

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 33.0)

        return layout
    

    # Run continuously to get webcam feed
    def update(self, *args):
        success, frame = self.capture.read()
        frame = frame[90 : 90 + 250, 240 : 240 + 250, :]

        buf = cv2.flip(frame, 0).tostring()
        img_texture = Texture.create(size = (frame.shape[1], frame.shape[0]), colorfmt = 'bgr')
        img_texture.blit_buffer(buf, colorfmt = 'bgr', bufferfmt = 'ubyte')
        self.web_cam.texture = img_texture


    # Preprocess the image before passing to the model
    def preprocess(self, file_path):
    
        # Read in image from file path
        byte_img = tf.io.read_file(file_path)
        
        # Load in the image 
        img = tf.io.decode_jpeg(byte_img)
        
        # Resizing the image 
        img = tf.image.resize(img, (105, 105))
        # Scale the image
        img = img / 255.0

        # Return image
        return img
    


    def verify(self, *args):
        # Threshold values
        detection_threshold = 0.5
        verification_threshold = 0.5

        # Capture input image from webcam
        save_path = os.path.join('application_data', 'input_image', 'input_image.jpg')
        ret, frame = self.capture.read()
        frame = frame[90 : 90 + 250, 240 : 240 + 250, :]
        cv2.imwrite(save_path, frame)

        # Result array
        results = []

        for image in os.listdir(os.path.join('application_data', 'verification_images')):
            input_img = self.preprocess(os.path.join('application_data', 'input_image', 'input_image.jpg'))
            validation_img = self.preprocess(os.path.join('application_data', 'verification_images', image))
            
            # Make prediction
            result = self.model.predict(list(np.expand_dims([input_img, validation_img], axis = 1)), verbose = 0)
            results.append(result)
        
        detection = np.sum(np.array(results) > detection_threshold)
        
        verification = detection / len(os.listdir(os.path.join('application_data', 'verification_images'))) 
        verified = verification > verification_threshold
        

        self.verification_label.text = 'verified' if verified == True else 'Unverified' 
        return results, verified
    



    



if __name__ == '__main__':
    CamApp().run()