import tensorflow as tf
# class MyDenseLayer(tf.keras.layers.Layer):
#   def __init__(self, num_outputs):
#     super(MyDenseLayer, self).__init__()
#     self.num_outputs = num_outputs
#
#   def build(self, input_shape,p):
#     print("build")
#     print(p)
#     print(self)
#     print(input_shape)
#     self.kernel = self.add_weight("kernel",
#                                   shape=[int(input_shape[-1]),
#                                          self.num_outputs])
#
#   def call(self, inputs):
#     return tf.matmul(inputs, self.kernel)
#
# layer = MyDenseLayer(10)
# layer.build(input_shape=[10,5],p='lwy')
# _ = layer(tf.zeros([10, 5]))
# print()
# x=tf.random.normal([1,8,3,96])
# y=tf.random.normal([1,8,3,96])
# c=x@(tf.transpose(y,[0,1,3,2]))
# print(c)
import vit_model
from tensorflow import keras
from tensorflow.keras import Sequential
a=([vit_model.Block(dim=768, num_heads=12, qkv_bias=None,
                             qk_scale=None, drop_ratio=0, attn_drop_ratio=0,
                             drop_path_ratio=0, name="encoderblock_{}".format(i))
                       for i in range(3)])
b=Sequential(*[([vit_model.Block(dim=768, num_heads=12, qkv_bias=None,
                             qk_scale=None, drop_ratio=0, attn_drop_ratio=0,
                             drop_path_ratio=0, name="encoderblock_{}".format(i))
                       for i in range(3)])])
c=[vit_model.Block(dim=768, num_heads=12, qkv_bias=None,
                              qk_scale=None, drop_ratio=0, attn_drop_ratio=0,
                              drop_path_ratio=0, name="encoderblock_{}".format(i))
                        for i in range(3)]
print(b)

