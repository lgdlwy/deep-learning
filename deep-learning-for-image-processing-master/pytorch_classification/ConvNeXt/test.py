from PIL import Image
import matplotlib.pyplot as plt
import torch
from torchvision import transforms
p=Image.open("D:/test.jpg")
p1=transforms.RandomResizedCrop(1000)(p)
plt.subplot(2,2,1)
plt.imshow(p1)
plt.show()