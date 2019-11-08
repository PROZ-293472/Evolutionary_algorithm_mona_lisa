from PIL import ImageDraw
import random
import math


class Square:

    def __init__(self, border_x=0, border_y=0, SwitchParam = False):
        self.border_x = border_x
        self.border_y = border_y
        if SwitchParam is False:
            self.color = []
            self.alpha = 0
            self.RGBA_color = tuple([*self.color, self.alpha])
            self.point = (0, 0)
            self.dim = (0, 0)
        else:
            self.color = [random.randint(0, 255) for k in range(3)]
            self.alpha = random.randint(0, 255)
            self.RGBA_color = tuple([*self.color, self.alpha])
            self.point = (random.randint(0, border_x), random.randint(0, border_y))
            self.dim = (random.randint(0, border_x-self.point[0]), random.randint(0, border_y-self.point[1]))   #TODO: CHECK!

    def draw(self, image):
        drw = ImageDraw.Draw(image, 'RGBA')
        drw.polygon([self.point,  (self.point[0], self.point[1] + self.dim[1]),
                     (self.point[0] + self.dim[0], self.point[1] + self.dim[1]),
                     (self.point[0] + self.dim[0], self.point[1])], fill=self.RGBA_color)

    def mutate_square(self, sigmas, n):
       # print("n =", n)
        if n>1:
            n=1
        elif n<-1:
            n=-1
        for i in range(0, 3):
            self.color[i] = math.floor(self.color[i] + sigmas.color[i] * n)
            if self.color[i] > 255:
                self.color[i] = 255
            elif self.color[i] < 0:
                self.color[i] = 0
        self.alpha = math.floor(self.alpha + sigmas.alpha * n)
        if self.alpha > 255:
            self.alpha = 255
        elif self.alpha < 0:
            self.alpha = 0
        self.RGBA_color = tuple([*self.color, self.alpha])
        self.point = (math.floor(self.point[0] + sigmas.point[0] * n), math.floor(self.point[1] + sigmas.point[1] * n))
        self.dim = (math.floor(self.dim[0] + sigmas.dim[0] * n), math.floor(self.dim[1] + sigmas.dim[1] * n))
        list_dim = list(self.dim)
        if list_dim[0] < 0:
            list_dim[0] = 0
        elif list_dim[0] > self.border_x:
            list_dim[0] = self.border_x
        if list_dim[1] < 0:
            list_dim[1] = 0
        elif list_dim[1] > self.border_y:
            list_dim[1] = self.border_y
        self.dim = tuple(list_dim)

        list_point = list(self.point)
        if list_point[0] < 0:
            list_point[0] = 0
        elif list_point[0] > self.border_x - self.dim[0]:
            list_point[0] = self.border_x - self.dim[0]
        if list_point[1] < 0:
            list_point[1] = 0
        elif list_point[1] > self.border_y - self.dim[1]:
            list_point[1] = self.border_y - self.dim[1]
        self.point = tuple(list_point)



class Sigma:
    def __init__(self, square=None):
        self.a = 0.05
        if square is None:
            self.color = []
            self.alpha = 0
            self.point = (0, 0)
            self.dim = [0, 0]
        else:

            self.color = [square.color[0] * self.a, square.color[1] * self.a, square.color[2] * self.a]
            self.alpha = self.a * square.alpha
            self.point = (square.point[0] * self.a, square.point[1] * self.a)
            self.dim = (square.dim[0] * self.a, square.dim[1] * self.a)

    def mutate_sigmas(self, tau, tau_prim, n1, n2):
        for i in range(0, 3):
            self.color[i] = self.color[i] * math.exp(tau * n1 + tau_prim * n2)
        self.alpha = self.alpha * math.exp(tau * n1 + tau_prim * n2)
        self.point = (self.point[0] * math.exp(tau * n1 + tau_prim * n2), self.point[1] * math.exp(tau * n1 + tau_prim * n2))
        self.dim = (self.dim[0] * math.exp(tau * n1 + tau_prim * n2), self.dim[1] * math.exp(tau * n1 + tau_prim * n2))


def average(s1, s2):
    if isinstance(s1, Square):
        s = Square()        #musza byc intami
        s.border_x = s1.border_x
        s.border_y = s1.border_y
        for i in range(0, len(s1.color)):
            s.color.append(((s1.color[i] + s2.color[i]) // 2))
        s.alpha = (s1.alpha + s2.alpha) // 2
        s.RGBA_color = tuple([*s.color, s.alpha])
        s.point = ((s1.point[0] + s2.point[0]) // 2, (s1.point[1] + s2.point[1]) // 2)
        s.dim = ((s1.dim[0] + s2.dim[0]) // 2, (s1.dim[1] + s2.dim[1]) // 2)
    else:
        s = Sigma()     #nie musza byc int'ami
        for i in range(0, len(s1.color)):
            s.color.append(((s1.color[i] + s2.color[i]) / 2))
        s.alpha = (s1.alpha + s2.alpha) / 2
        s.RGBA_color = tuple([*s.color, s.alpha])
        s.point = ((s1.point[0] + s2.point[0]) / 2, (s1.point[1] + s2.point[1]) / 2)
        s.dim = ((s1.dim[0] + s2.dim[0]) / 2, (s1.dim[1] + s2.dim[1]) / 2)

    return s
