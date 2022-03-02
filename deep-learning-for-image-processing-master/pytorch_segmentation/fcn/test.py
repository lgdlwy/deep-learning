import numpy as np
import torch.nn as nn
import torch
a=torch.FloatTensor([[1,2,3],[4,5,6],[7,8,9]]).reshape(1,1,3,3)
print(nn.functional.interpolate(a,size=(2,2),mode='bilinear',align_corners=True))
print(nn.functional.interpolate(a,size=(2,2),mode='bilinear',align_corners=False))