import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
# a=tf.Variable(initial_value=tf.random_normal_initializer()([32,28,28,6]))
# a=tf.reshape(a,[32,28,28,3,2])
# print(a.shape)
def test(a,b:int=2):
    return a+b
c=test(1)
print(c)