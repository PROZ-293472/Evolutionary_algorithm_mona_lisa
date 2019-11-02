import numpy as np
from PIL import Image

from src.entities.square import Square

im = Image.open('mona.png')
#im.show()
arr = np.asarray(im)
#print(arr)
#print(arr.dtype)
img = Image.new('RGB', (500, 500))

im1 = Image.fromarray(arr)
im1 = im1.convert('RGB')
arr1 = np.asarray(im1)
sqr  = Square()
#print(arr1.shape)

b = np.array([[[1,2,3],[4,5,6],[7,8,9]] , [[11,12,13],[14,15,16],[17,18,19]]])
(a,b,c) = (np.sum(b[0, :, :]), b[0, 1, 0], b[0, 0, 1])
print(a)
#[warstwa, rzad, kolumna]

im2 = Image.new('RGB', (357, 500), (255,255,255))
arr2 = np.asarray(im2)
#print(np.subtract(arr2, arr)[0,:])
arr3 = np.subtract(arr2, arr)
im3 = Image.fromarray(arr3)
#im3.show()