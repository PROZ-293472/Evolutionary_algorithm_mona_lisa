from src.entities.square import average
from src.entities.specimen import Specimen
from src.entities.population import Population
import random
import numpy as np


def crossover(temp):
    reproduced = Population()
    for i in range(0, len(temp.specimen)):
        if i == len(temp.specimen) - 1:
            s1 = temp.specimen[i]
            s2 = temp.specimen[0]
        else:
            s1 = temp.specimen[i]
            s2 = temp.specimen[i+1]
        s = Specimen(s1.square_num, s1.image_x, s1.image_y, True)

        for j in range(0, s1.square_num):
            s.squares.append(average(
                s1.squares[j],
                s2.squares[j]))
            s.sigmas.append(average(s1.sigmas[j], s2.sigmas[j]))

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


def generate_random(population, l):
    temporary = Population()
    for i in range(0, l):
        temporary.specimen.append(random.choice(population.specimen))
    return temporary


# Returns new population of size miu
def selection(population_r, target_image, miu):
    population_size = len(population_r.specimen)
    fitness_list = population_r.get_fitness(target_image)
    fitness_sum = sum(fitness_list)
    norm_fitness_list = [fitness_list[i]/fitness_sum for i in range(0, population_size)]
    # print(norm_fitness_list)



