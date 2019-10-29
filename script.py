import numpy as np
from PIL import Image

im = Image.open('mona.png')
im.show()
arr = np.asarray(im)
print(arr.shape)
print(arr.dtype)

im1 = Image.fromarray(arr)
im1.show()