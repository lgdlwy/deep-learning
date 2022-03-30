import torch
import random
# b=torch.tensor([[35,37,499,272]])
# print(b.shape)
# print(b[0,3])
# print(b[:,[1]])
# print(random.sample(range(0, 500), k=5))
# a=torch.randn([3,4])
# b,c,d,e=a.unbind(1)
# print(b,c,d,e)
# a=[[3, 800, 1066], [3, 900, 1066], [3, 800, 1066], [3, 800, 1066], [3, 800, 1066], [3, 800, 1066], [3, 800, 1066], [3, 800, 1066]]
# # print(a[0])
# # b=a[0]
# # for sublist in a[1:]:
# #     print(sublist)
# #     for index, item in enumerate(sublist):
# #         b[index] = max(b[index], item)
# print([1,2,3]+[8])
# a=torch.randn([3,800,1066])
# b=a.new_full([8, 3, 800, 1216], 0)
# print(b.shape)
# print(a.shape)
# a=[1,2,3]
# b=[4,5,6]
# c=zip(a,b)
# for i,j in c:
#     print(i,j)
# print(*d)
# print(c)
from PIL import Image
a=Image.open("D:/4.jpg")
print()