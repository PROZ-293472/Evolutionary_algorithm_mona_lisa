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

img = Image.new('RGB', (500, 500), (255, 255, 255))
for i in range(1, 100):
    sqr = Square(500, 500)
    sqr.draw(img)
#img = img.convert('RGB')
img.show()

arr = np.asarray(img) #TODO <--- TUTAJ SIE WYDUPIA
print(arr)
im = Image.fromarray(arr)
im.show()
img2 = Image.new('RGB', (500, 500), (255, 255, 255))

#(err_R, err_G, err_B) = TargetFunction.calculate_error(img_arr, target_arr)
#print((err_R, err_G, err_B))


#b = np.array([[[1,2,3],[4,5,6],[7,8,9]] , [[11,12,13],[14,15,16],[17,18,19]]])
#(a,b,c) = (np.sum(b[0, :, :]), b[0, 1, 0], b[0, 0, 1])
#print(a)
#[warstwa, rzad, kolumna]

im = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\PSZT-1\\content\\mona.png')
print(im.size)
arr = np.asarray(im)
im2 = Image.new('RGB', (357, 500), (255,255,255))
arr2 = np.asarray(im2)
arr3 = np.subtract(arr2, arr)
np.savetxt('mona_test.out', arr[2])
im3 = Image.fromarray(arr3)
#im3.show()

(err_R, err_G, err_B) = TargetFunction.calculate_error(arr, arr2)
print((err_R, err_G, err_B))