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
        pass

if __name__ == '__main__':
    CamApp().run()