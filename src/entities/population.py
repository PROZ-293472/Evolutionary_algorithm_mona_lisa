from src.entities.specimen import Specimen
from src.entities.targetfun import *


class Population:
    def __init__(self, miu=0, square_num=0, image_x=0, image_y=0, specimen = None):
        if specimen:
            self.specimen = specimen
        else:
            self.specimen = []
            if miu != 0:
                for i in range(0, miu):
                    self.specimen.append(Specimen(square_num, image_x, image_y))

    def get_images(self):
        images = []
        for s in self.specimen:
            images.append(s.get_image())
        return images

    def get_images_arrays(self):
        arrays = []
        for s in self.specimen:
            arrays.append(np.asarray(s.get_image()))
        return arrays

    def get_fitness(self, target_img):
        fitness = []
        for s in self.specimen:
            fitness.append(TargetFunction.target_function(np.asarray(s.get_image()), target_img))
        return fitness

    def merge(self, population):
        new_specimen = self.specimen + population.specimen
        return Population(specimen= new_specimen)
