import tensorflow as tf
from tensorflow import keras
import os
import torch.nn as nn
import torch
from tensorflow.python import pywrap_tensorflow
# with tf.Graph().as_default(), tf.compat.v1.Session().as_default() as sess:
#     var_list = tf.train.list_variables("./save_weights/resNet_50")
#     new_var_list = []
#     for var_name, shape in var_list:
#         print(var_name)
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(5, input_shape=(3,)),
#     tf.keras.layers.Softmax()])
# model.save('model')
# sequential_model = keras.Sequential(
#     [
#         keras.Input(shape=(784,), name="digits"),
#         keras.layers.Dense(64, activation="relu", name="dense_1"),
#         keras.layers.Dense(64, activation="relu", name="dense_2"),
#         keras.layers.Dense(10, name="predictions"),
#     ]
# )
# sequential_model.save_weights("ckpt")
# load_status = sequential_model.load_weights("ckpt")


# with tf.Graph().as_default(), tf.compat.v1.Session().as_default() as sess:
#
#     var_list = tf.train.list_variables('resnet_v1_50.ckpt')
#     new_var_list = []
#     i=0
#     for var_name, shape in var_list:
#         i+=1
#         print(var_name,shape)
#     print(i)

    # var_list = tf.train.list_variables('3.ckpt')
    # new_var_list = []
    # for var_name, shape in var_list:
    #     print(var_name, shape)
a=torch.randn(1,2,3,4)
b=nn.LayerNorm([2,3])

d=b(a)

print(d)
