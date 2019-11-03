from PIL import Image
import copy
import random
import numpy as np
import math
from PIL import Image, ImageDraw
from src.entities.square import Square
from src.entities.square import average_square

# TODO: M
#       Michał: Funkcja celu, kwadraty + funkcja konwersji
#
#
#


class Population:
    def __init__(self, child=False, miu=0, square_num=0, image_x=0, image_y=0):
        # Generate population
        print('Generating population of size:', miu)
        self.specimen = []
        if not child:
            for i in range(0, miu):
                self.specimen.append(Specimen(square_num, image_x, image_y))

    def show_specimen(self):
        for s in self.specimen:
            s.get_image().show()


def generate_random(population, l):
    temporary = Population(True)
    for i in range(l):
        temporary.specimen.append(random.choice(population.specimen))
    return temporary

def crossover(temp):
    # Dobieraj osobniki w pary 1 z 2, 2 z 3, 3 z 1
    reproduced = Population(True)
    for i in range(0, len(temp.specimen)):
        if i == len(temp.specimen) - 1:
            s1 = temp.specimen[i]
            s2 = temp.specimen[0]
        else:
            s1 = temp.specimen[i]
            s2 = temp.specimen[i+1]
        s = Specimen(s1.square_num, s1.image_x, s1.image_y, True)

        for j in range(0, s1.square_num):
            s.squares.append(average_square(s1.squares[j], s2.squares[j]))
            s.sigmas.append(average_sigma(s1.sigmas[j], s2.sigmas[j]))

        reproduced.specimen.append(s)
    return reproduced


def mutation(reproduced, tau, tau_prim):
    for spec in reproduced.specimen:
        n = np.random.normal(0, 1, len(spec.squares))
        n1 = np.random.normal(0, 1, len(spec.squares))
        n2 = np.random.normal(0, 1, len(spec.squares))
        for i in range(0, len(spec.squares)):
            spec.sigmas[i].mutate_sigmas(tau, tau_prim, n1[i], n2[i])
            spec.squares[i].mutate_square(spec.sigmas[i], n[i])
    return reproduced

class Sigma:
    def __init__(self, square=None):
        self.a = 0.1
        if square is None:
            self.color_sigma = []
            self.alpha_sigma = 0
            self.point_sigma = (0, 0)
            self.dim_sigma = [0, 0]
        else:

            self.color_sigma = [square.color[0] * self.a, square.color[1] * self.a, square.color[2] * self.a]
            self.alpha_sigma = self.a * square.alpha
            self.point_sigma = (square.point[0] * self.a, square.point[1] * self.a)
            self.dim_sigma = [square.dim[0] * self.a, square.point[1] * self.a]

    def mutate_sigmas(self, tau, tau_prim, n1, n2):
        for i in range(0,3):
            self.color_sigma[i] = self.color_sigma[i] * math.exp(tau * n1 + tau_prim * n2)
        self.alpha_sigma = self.alpha_sigma * math.exp(tau * n1 + tau_prim * n2)
        self.point_sigma = (self.point_sigma[0] * math.exp(tau * n1 + tau_prim * n2),
                            self.point_sigma[1] * math.exp(tau * n1 + tau_prim * n2))
        self.dim_sigma = [self.dim_sigma[0] * math.exp(tau * n1 + tau_prim * n2),
                          self.dim_sigma[1] * math.exp(tau * n1 + tau_prim * n2)]


def average_sigma(s1, s2):
    s = Sigma()
    for i in range(0, len(s1.color_sigma)):
        s.color_sigma.append(((s1.color_sigma[i] + s2.color_sigma[i]) // 2))
    s.alpha_sigma = (s1.alpha_sigma + s2.alpha_sigma) // 2
    s.point_sigma = ((s1.point_sigma[0] + s2.point_sigma[0]) / 2, (s1.point_sigma[1] + s2.point_sigma[1]) // 2)
    s.dim_sigma = [(s1.dim_sigma[0] + s2.dim_sigma[0]) / 2, (s1.dim_sigma[1] + s2.dim_sigma[1]) // 2]
    return s
# Member of a population
class Specimen:
    def __init__(self, square_num, image_x, image_y, child=False):
        # Generate one member of a population - specimen(image)
        self.image_x = image_x
        self.image_y = image_y
        self.squares = []
        self.square_num = square_num
        self.image = Image.new('RGB', (image_x, image_y), (255, 255, 255))
        self.sigmas = []

        if not child:
            for i in range(square_num):
                self.squares.append(Square(image_x, image_y))
                self.sigmas.append(Sigma((self.squares[i])))


    def get_image(self):
        background = Image.new('RGB', (self.image_x, self.image_y), (255, 255, 255))
        for s in self.squares:
            s.draw(background)
        return background


# Check if algorithm should stop
def is_stop(p):
    return False


def create_target(image):
    arr = np.asarray(image)
    return arr


def calculate_error(rgba_map, target_map):
    sub = np.subtract(rgba_to_rgb(rgba_map), target_map)
    (raw_errR, raw_errG, raw_errB) = (np.sum(sub[0, :, :]), np.sum(sub[1, :, :]), np.sum(sub[2, :, :]))
    # TODO: Wymyslec, w jaki sposob normalizowac bledy
    return raw_errR, raw_errG, raw_errB


def rgba_to_rgb(rgba_map):
    img = Image.fromarray(rgba_map)
    img = img.convert('RGB')
    return np.asarray(img)


def main():
    print("starting algorithm")
    u = 1  # miu
    l = 1  # lambda

    prostokaty = 100
    tau = 1/ (math.sqrt(prostokaty*2))
    tau_prim = 1/ (math.sqrt(2* math.sqrt(prostokaty)))
    image_x = 1000
    image_y = 1000
    population = Population(False, u, prostokaty, image_x, image_y)

    temporary = generate_random(population, l)
    temporary.show_specimen()
    for i in range(100):
        reproduced = crossover(temporary)
        reproduced = mutation(reproduced, tau, tau_prim)
    reproduced.show_specimen()





# TODO: 1. wybrac populacje o dobrej wielkosci - funkcja generate_random() - done
#       2. Utworzenie potomnej populacji:
#             2.1 Krzyżowanie - done, wersja 1. czyli usrednienie rodzicow
#             2.2 Mutacja
#       3. Wybór nowej populacji


if __name__ == '__main__':
    main()
