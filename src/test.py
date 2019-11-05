import numpy as np
import math
from PIL import Image
import psutil
import time
from src.modules.algorithm import *


# Check if algorithm should stop
def is_stop(p):
    return False




def main():

    population_size = 5  # miu
    reproduced_size = 7  # lambda
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

    images = population_r.get_images()
    for i in images:
        i.show()


if __name__ == '__main__':
    main()
