from PIL import Image, ImageDraw
import random
import math
import numpy as np

# Zmienne:
# kolor + alpha
# pozycja
# wymiary
class Square:

    def __init__(self, border_x=0, border_y=0):
        if border_x == 0 and border_y == 0:
            self.color = []
            self.alpha = 0
            self.RGBA_color = tuple([*self.color, self.alpha])
            self.point = (0, 0)  # TODO: CHECK!
            self.dim = [0, 0]  # TODO: CHECK!
        else:
            self.color = [random.randint(0, 255) for k in range(3)]
            self.alpha = random.randint(0, 100)
            self.RGBA_color = tuple([*self.color, self.alpha])
            self.point = (random.randint(0, border_x), random.randint(0, border_y))   #TODO: CHECK!
            self.dim = [random.randint(0, border_x-self.point[0]), random.randint(0, border_y-self.point[1])]   #TODO: CHECK!

    def draw(self, image):
        drw = ImageDraw.Draw(image, 'RGBA')
        drw.polygon([self.point,  (self.point[0], self.point[1] + self.dim[1]),
                     (self.point[0] + self.dim[0], self.point[1] + self.dim[1]),
                     (self.point[0] + self.dim[0], self.point[1])], fill=self.RGBA_color)

    def mutate_square(self, sigmas, n):
        for i in range(0, 3):
            self.color[i] = self.color[i] + sigmas.color_sigma[i] * n
        self.alpha = self.alpha + sigmas.alpha_sigma * n
        self.point = (self.point[0] + sigmas.point_sigma[0] * n, self.point[1] + sigmas.point_sigma[1] * n)
        self.dim = [self.dim[0] + sigmas.dim_sigma[0] * n, self.dim[1] + sigmas.dim_sigma[1] * n]


# uśrednij dwa kwadraty
def average_square(s1, s2):
    s = Square()
    for i in range(0, len(s1.color)):
        s.color.append(((s1.color[i] + s2.color[i])//2))
    s.alpha = (s1.alpha + s2.alpha)//2
    s.RGBA_color = tuple([*s.color, s.alpha])
    s.point = ((s1.point[0] + s2.point[0])/2, (s1.point[1] + s2.point[1])//2)
    s.dim = [(s1.dim[0] + s2.dim[0])/2, (s1.dim[1] + s2.dim[1])//2]
    return s

