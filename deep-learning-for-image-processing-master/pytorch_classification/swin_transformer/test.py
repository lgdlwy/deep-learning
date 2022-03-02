import torch
import tensorflow as tf
import numpy as np
# input = torch.randn(20, 5, 10, 10)
# m=torch.nn.LayerNorm(10)
# output=m(input)
# print(output.shape)
# x = torch.tensor([1, 2, 3])
# y = torch.tensor([4, 5, 6])
# grid_x, grid_y = torch.meshgrid(x, y,indexing='ij')
# x=torch.range(0,11).reshape(3,4,1)
# print(x)
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5])

grid_x, grid_y = torch.meshgrid(x, y, indexing='ij')
print(grid_x)
print(grid_y)
grid_x, grid_y = torch.meshgrid(x, y,indexing='xy')
print(grid_x)
print(grid_y)
torch.equal(torch.cat(tuple(torch.dstack([grid_x, grid_y]))),
            torch.cartesian_prod(x, y))

import matplotlib.pyplot as plt
xs = torch.linspace(-5, 5, steps=100)
ys = torch.linspace(-5, 5, steps=100)
x, y = torch.meshgrid(xs, ys, indexing='xy')
z = torch.sin(torch.sqrt(x * x + y * y))
ax = plt.axes(projection='3d')
ax.plot_surface(x.numpy(), y.numpy(), z.numpy())
plt.show()


