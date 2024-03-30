# Custom distance layer


# Importing necessary libraries
from tensorflow.keras.layers import Layer
import tensorflow as tf

# Distance layer
class Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()
       
    # Similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)