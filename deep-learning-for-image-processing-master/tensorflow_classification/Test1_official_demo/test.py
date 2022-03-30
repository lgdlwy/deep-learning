import tensorflow as tf
import numpy as np
b=tf.random.normal([1,10,200])
c=np.random.randn(3,200,512)

a=tf.nn.conv1d(tf.cast(b,tf.float32),tf.cast(c,tf.float32),1,'SAME')
print(a.shape)