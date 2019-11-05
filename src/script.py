import numpy as np
from PIL import Image, ImageDraw

from src.entities.helpers import ImageHelper
from src.entities.square import Square

#im = Image.open('mona.png')
#im.show()
#arr = np.asarray(im)
#print(arr)
#print(arr.dtype)
#img.show()
from src.entities.targetfun import TargetFunction

dim = 500
img = Image.new('RGB', (dim, dim), (255, 255, 255))
for i in range(0, 100):
    sqr = Square(dim, dim)
    # print(sqr.dim)
    # print(sqr.RGBA_color)
    sqr.draw(img)
#img = img.convert('RGB')
img.show()

arr = np.asarray(img)
# print(arr[:,:,2])

img2 = Image.new('RGB', (dim, dim), (255, 255, 255))
target_arr = np.asarray(img2)
print(TargetFunction.target_fucntion(arr,target_arr))

color_errors = TargetFunction.calculate_error(arr, target_arr)
print(color_errors)

# macierz = np.array([[[1,2,3],[4,5,6],[7,8,9]] , [[11,12,13],[14,15,16],[17,18,19]]])
# (a,b,c) = (np.sum(macierz[0, :, :]), macierz[0, 1, 0], macierz[0, 0, 1])
# print(a)
#[warstwa, rzad, kolumna]

# im = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\PSZT-1\\content\\mona.png')
# print(im.size)
# arr = np.asarray(im)
# im2 = Image.new('RGB', (357, 500), (255,255,255))
# arr2 = np.asarray(im2)
# arr3 = np.subtract(arr2, arr)
# np.savetxt('mona_test.out', arr[2])
# im3 = Image.fromarray(arr3)
# #im3.show()

# (err_R, err_G, err_B) = TargetFunction.calculate_error(arr, arr2)
# print((err_R, err_G, err_B))