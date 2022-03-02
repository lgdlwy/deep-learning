import torch
from torch import nn
import vit_model
from vit_model import Block
# dpr = [x.item() for x in torch.linspace(0, 0.2, 12)]
# print(dpr)
a=[
            Block(dim=1, num_heads=1, mlp_ratio=1, qkv_bias=None, qk_scale=4,
                  drop_ratio=0.2, attn_drop_ratio=0, drop_path_ratio=0,
                  norm_layer=nn.LayerNorm, act_layer=nn.Tanh)
             for i in range(12)
        ]
print(a)
# blocks = nn.Sequential([
#             Block(dim=1, num_heads=1, mlp_ratio=1, qkv_bias=None, qk_scale=4,
#                   drop_ratio=0.2, attn_drop_ratio=0, drop_path_ratio=0,
#                   norm_layer=nn.LayerNorm, act_layer=nn.Tanh)
#             # for i in range(12)
#         ])
# print(blocks)
# x=torch.randn(3,197,768)
# c=x[:,0,:]
# print(x[:,0,:])
# b=x[:,0]
# print(torch.equal(b,c))