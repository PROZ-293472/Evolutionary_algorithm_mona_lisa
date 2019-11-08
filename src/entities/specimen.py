from src.entities.square import Square
from src.entities.square import Sigma
from PIL import Image


class Specimen:
    def __init__(self, square_num, image_x, image_y, child=False):
        # Generate one member of a population - specimen(image)
        self.image_x = image_x
        self.image_y = image_y
        self.squares = []
        self.square_num = square_num
        self.image = Image.new('RGB', (image_x, image_y), (0, 0, 0))
        self.sigmas = []

        if not child:
            for i in range(square_num):
                self.squares.append(Square(image_x, image_y, True))
                self.sigmas.append(Sigma((self.squares[i])))

    def get_image(self):
        background = Image.new('RGB', (self.image_x, self.image_y), (0, 0, 0))
        for s in self.squares:
            s.draw(background)
        return background


