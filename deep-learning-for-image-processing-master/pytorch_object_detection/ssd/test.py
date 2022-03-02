# 只做测试
import torch
from torch import nn
kernel=torch.randn([3,1,3*3,7,7])
x_folded=torch.randn([3,12//3,3*3,7,7])
y=kernel*x_folded
print(y.shape)
out=y.sum(dim=2)
print(out.shape)
out=out.view(12,7,7)
print(out.shape)




