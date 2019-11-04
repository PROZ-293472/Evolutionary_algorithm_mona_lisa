import numpy as np
import math
from PIL import Image
import psutil
import time
from src.modules.algorithm import *


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

    population_size = 3  # miu
    reproduced_size = 4  # lambda
    dimension = 1000         #number of squares
    tau = 1 / (math.sqrt(dimension*2))
    tau_prim = 1 / (math.sqrt(2 * math.sqrt(dimension)))
    image_x = 700          #size of target image
    image_y = 700

    population_p = Population(population_size, dimension, image_x, image_y)
    images = population_p.get_images()
    for i in images:
        i.show()

    for i in range(0, 100):
        population_t = generate_random(population_p, reproduced_size)
        population_r = crossover(population_t)
        population_r = mutation(population_r, tau, tau_prim)
        population_p = population_r         #tutaj selekcja

    images = population_p.get_images()
    for i in images:
        i.show()


if __name__ == '__main__':
    main()
