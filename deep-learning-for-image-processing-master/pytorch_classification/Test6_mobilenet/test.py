import torch
import tensorflow as tf
from tensorflow.keras import layers
a=torch.randn([3,3,32,32])
kernel=9
stride=5
padding=(kernel-1)//2
b=torch.nn.Sequential(
    torch.nn.Conv2d(3,3,kernel_size=kernel,stride=stride,padding=padding)
)
print(b(a).shape)
c=tf.Variable(tf.random_normal_initializer()([3,32,32,3]))
d=layers.Conv2D(filters=3,
                kernel_size=kernel,
                strides=(stride,stride),
                padding='same')
print(d(c).shape)
