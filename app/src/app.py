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
        self.web_cam = Image(size_hint = (1, .8))
        self.button = Button(text = 'Verify', size_hint = (1, 0.1))
        self.verification_label = Label(text = 'Verification Uninitiated', size_hint = (1, 0.1))


        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)

        return layout

if __name__ == '__main__':
    CamApp().run()