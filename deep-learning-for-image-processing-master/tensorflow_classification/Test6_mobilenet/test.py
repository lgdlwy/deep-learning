from __future__ import absolute_import, division, print_function
import tensorflow as tf
import model_v3
from tensorflow.keras import layers
import keras.applications
# stride=1
# inputsize=34
# kernel_size=4
# import tensorflow.python.keras.applications.imagenet_utils
# # a=tf.convert_to_tensor(tf.Variable(tf.random_normal_initializer()([5,5,5,5])))
# a=(tf.Variable(tf.random_normal_initializer()([1,inputsize,inputsize,1])))
# b=layers.ZeroPadding2D(padding=model_v3.correct_pad(inputsize, kernel_size))(a)
# # b=tf.convert_to_tensor(tf.Variable(tf.random_normal_initializer()([5,1,1,5])))
# #
# # print(layers.Multiply()([a,b]).shape)
# print(b.shape)
#
# x = layers.DepthwiseConv2D(kernel_size=kernel_size,
#                            strides=stride,
#                            padding='same' if stride == 1 else 'valid',
#                            use_bias=False,
#                            )
# print(x(b).shape)

import tensorflow as tf
tf.keras.backend.clear_session()
import tensorflow.keras as keras
import tensorflow.keras.layers as layers

class MyLayer(layers.Layer):
   def __init__(self, unit=32):
       super(MyLayer, self).__init__()
       self.unit = unit

   def build(self, input_shape):
       print('build')
       self.weight = self.add_weight(shape=(input_shape[-1], self.unit),
                                     initializer=keras.initializers.RandomNormal(),
                                     trainable=True)
       self.bias = self.add_weight(shape=(self.unit,),
                                   initializer=keras.initializers.Zeros(),
                                   trainable=True)

   def call(self, inputs):
       print('call')
       return tf.matmul(inputs, self.weight) + self.bias

my_layer = MyLayer(3)
x = tf.ones((3,5))
out = my_layer(x)
print(out)
out=my_layer(x)


