import os
from numpy.random import random
import numpy as np

import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a racoon!
from PIL import Image  # for reading image files

# numpy ndarrays

my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array.shape)
print(my_array[2])
print(my_array.ndim)

# 2-dimensional (matrix)

array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

print(array_2d[1, 2])  # Access 3rd value in 2nd row
print(array_2d[0, :])  # Access all the values in the first row

# n-dimensional (tensor)

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'We have {mystery_array.ndim} dimensions')
print(f'The shape is {mystery_array.shape}')

print(mystery_array[2, 1, 3])

print(mystery_array[2, 1, :])

print(mystery_array[:, :, 0])

# numpy challenges

# Challenge 1
a = np.arange(10, 30)
print(a)

# Challenge 2
print(a[-3:])
print(a[3:6])
print(a[12:])
print(a[::2])

# Challenge 3
print(np.flip(a))
print(a[::-1])

# Challenge 4
b = np.array([6, 0, 9, 0, 0, 5, 0])
nz_indices = np.nonzero(b)
print(nz_indices)

# Challenge 5
z = random((3, 3, 3))
print(z)
print(z.shape)

# Challenge 6
x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# Challenge 7
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

# Challenge 8
noise = np.random.random((128, 128, 3))
print(noise.shape)
plt.imshow(noise)

# Linear Algebra

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

print(v1 + v2)

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

print(list1 + list2)

print(v1 * v2)

# Gives an error
# print(list1 * list2)

# Broadcasting and scalars
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
print(array_2d)

print(array_2d + 10)

print(array_2d * 5)

# Matrix Multiplication

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

c = np.matmul(a1, b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
print(c)

print(a1 @ b1)

# Manipulating images

img = misc.face()
plt.imshow(img)

print(type(img))
print(img.shape)
print(img.ndim)

grey_vals = np.array([0.2126, 0.7152, 0.0722])
sRGB_array = img / 255
# or: img_gray = np.matmul(sRGB_array, grey_vals)
img_gray = sRGB_array @ grey_vals

plt.imshow(img_gray)

plt.imshow(img_gray, cmap="gray")

plt.imshow(np.flip(img_gray), cmap='gray')

plt.imshow(np.rot90(img))

solar_img = 255 - img
plt.imshow(solar_img)


LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

file_name = 'images/yummy_macarons.jpg'

my_img = Image.open(os.path.join(LOCATION, file_name))
img_array = np.array(my_img)

print(img_array.ndim)
print(img_array.shape)

plt.imshow(img_array)

plt.imshow(255-img_array)
