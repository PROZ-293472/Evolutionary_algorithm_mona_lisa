import random
from src.entities.specimen import Specimen


class Population:
    def __init__(self, miu=0, square_num=0, image_x=0, image_y=0):
        self.specimen = []
        if miu != 0:
            for i in range(0, miu):
                self.specimen.append(Specimen(square_num, image_x, image_y))

    def get_images(self):
        images = []
        for s in self.specimen:
            images.append(s.get_image())
        return images


