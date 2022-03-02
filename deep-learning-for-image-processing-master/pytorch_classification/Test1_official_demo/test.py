import torch
# a = torch.rand(3,3)
# b = a.permute(1,0)
# c = b.reshape(9)
# c[0]=100
# print(a,b,c)

a = torch.arange(9).reshape(3, 3)      # 初始化张量a
print('storage of a:\n', a.storage())
