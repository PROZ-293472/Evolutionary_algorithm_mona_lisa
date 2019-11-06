import math
from PIL import Image
from src.modules.algorithm import *
from src.entities.targetfun import *
from src.entities.square import Square


# Check if algorithm should stop
def is_stop(p):
    return False


def main():
    target_image = Image.open("mona.png")
    # target_image.show()
    target_image = np.asarray(target_image)
    population_size = 10  # miu
    reproduced_size = 4  # lambda
    dimension = 1000         # number of squares
    tau = 1 / (math.sqrt(dimension*2))
    tau_prim = 1 / (math.sqrt(2 * math.sqrt(dimension)))
    image_x = 357          # size of target image
    image_y = 500

    img = Image.new('RGB', (image_x, image_y), (255, 255, 255))

    # for i in range(1, 50):
    #     s = Square(image_x, image_y)
    #     s.draw(img)
    # img.show()
    # print(img.format)
    # print(img.size)
    # TargetFunction.calculate_error(np.asarray(img), target_image)

    population_p = Population(population_size, dimension, image_x, image_y)
    # selection(population_p, target_image, reproduced_size)
    images = population_p.get_images()
    # for i in images:
    #     i.show()

    for i in range(0, 10):
        population_t = generate_random(population_p, reproduced_size)
        population_r = crossover(population_t)
        population_r = mutation(population_r, tau, tau_prim)
        population_p = selection(population_r, population_p, target_image, population_size)         # tutaj selekcja

    images = population_p.get_images()
    for i in images:
        i.show()


if __name__ == '__main__':
    main()
