import math
from PIL import Image
from src.modules.algorithm import *
from src.entities.targetfun import *
from src.entities.square import Square


# Check if algorithm should stop
def is_stop(p):
    return False


def test_mutation():
    pop = Population(1, 1, 500, 500)
    tau = 1 / (math.sqrt(1 * 2))
    tau_prim = 1 / (math.sqrt(2 * math.sqrt(1)))
    pop.get_images()[0].show()
    spr = pop.specimen[0].squares[0]
    sig = pop.specimen[0].sigmas[0]
    print(spr.color, spr.alpha, spr.point, spr.dim)
    print(sig.color, sig.alpha, sig.point, sig.dim)
    pop = mutation(pop, tau, tau_prim)
    spr = pop.specimen[0].squares[0]
    sig = pop.specimen[0].sigmas[0]
    print(spr.color, spr.alpha, spr.point, spr.dim)
    print(sig.color, sig.alpha, sig.point, sig.dim)
    pop.get_images()[0].show()



def main():
    #target_image = Image.open("mona.png")
    target_image = Image.new('RGB', (357,500), (255, 0, 0))
    # temp_image = Image.new('RGB', (357, 500), (255,255,255))
    # # target_image.show()
    target_image = np.asarray(target_image)
    # temp_image = np.asarray(temp_image)
    # target_image = np.subtract(temp_image,target_image)

    population_size = 20  # miu
    reproduced_size = 25  # lambda
    dimension = 1       # number of squares
    tau = 1 / (math.sqrt(dimension*2))
    tau_prim = 1 / (math.sqrt(2 * math.sqrt(dimension)))
    image_x = 357          # size of target image
    image_y = 500



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
    #for i in images:
    #    i.show()
    # for i in images:
    #     i.show()

    for i in range(0, 50):
        print(sum(population_p.get_fitness(target_image)))
        population_t = generate_random(population_p, reproduced_size)
        # for i in population_t.get_images():
        #     i.show()

        population_r = crossover(population_t)
        # for i in population_r.get_images():
        #     i.show()

        spr = population_r.specimen[0].squares[0]
        sig = population_r.specimen[0].sigmas[0]
        print(spr.color, spr.alpha, spr.point, spr.dim)
        print(sig.color, sig.alpha, sig.point, sig.dim)
        population_r = mutation(population_r, tau, tau_prim)
        spr = population_r.specimen[0].squares[0]
        sig = population_r.specimen[0].sigmas[0]
        print(spr.color, spr.alpha, spr.point, spr.dim)
        print(sig.color, sig.alpha, sig.point, sig.dim)
       # population_r.get_images()[0].show()


        #
        # for i in population_r.get_images():
        #     i.show()
        population_p = selection(population_r, population_p, target_image, population_size) # tutaj selekcja
    images = population_p.get_images()
    for i in images:
        i.show()


if __name__ == '__main__':
    main()
    #test_mutation()
