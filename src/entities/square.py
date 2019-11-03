from PIL import Image, ImageDraw
import random


class Square:

    def __init__(self, border_x, border_y):
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

