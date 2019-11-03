from PIL import Image
import copy

import numpy as np
from PIL import Image, ImageDraw

# TODO: Mateusz: Krzyżowanie, mutacja,
#       Michał: Funkcja celu, kwadraty + funkcja konwersji
#
#
#


class Population:
    def __init__(self, miu, square_num, image_x, image_y):
        # Generate population
        print('Generating population of size:', miu)
        specimen = []
        for i in range(0, miu):
            specimen.append(Specimen(square_num, image_x, image_y))


# Member of a population
class Specimen:
    def __init__(self, square_num, image_x, image_y):
        # Generate one member of a population - specimen(image)
        self.squares = []
        self.sigmas = np.zeros(square_num);
        for i in range(square_num):
            self.squares.append(Square(100, 100))
            self.rgbmap = np.zeros((image_x, image_y, 3), dtype=np.uint8) + 255
            print(self.rgbmap.shape)
            #self.image = Image.fromarray(self.rgbmap)
            #self.image.show()



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
    u = 10  # miu
    l = 12  # lambda
    prostokaty=100
    image_x=100
    image_y=100
    population = Population(u, prostokaty, image_x, image_y)

    # Algorith
    while not is_stop(population):
        # TODO: 1. wybrac populacje o dobrej wielkosci - funkcja generate_random()
        #       2.
        #
        # Create temporary population T
        temporary_population = population.generate_random(l)

        # Selection: crossover, mutation then selection
        reproduced = temporary_population.selection()
        population = reproduced
    else:
        # If the stop condition is met, return best specimen
        best = population.get_best()

if __name__ == '__main__':
    main()