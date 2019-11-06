import math

import numpy as np
from PIL import Image


class TargetFunction:

    @staticmethod
    def target_function(image, target_image):
        image_array = np.asarray(image)
        target_image = np.asarray(target_image)
        errors = TargetFunction.calculate_error(image_array, target_image)
        temp = 0
        for err in errors:
            temp += math.pow(err, 2)
        return math.sqrt(temp)

    @staticmethod
    def calculate_error(pic_matrix, target_matrix):
        R_pic = int(np.sum(pic_matrix[:, :, 0]))
        G_pic = int(np.sum(pic_matrix[:, :, 1]))
        B_pic = int(np.sum(pic_matrix[:, :, 2]))

        R_tar = int(np.sum(target_matrix[:, :, 0]))
        G_tar = int(np.sum(target_matrix[:, :, 1]))
        B_tar = int(np.sum(target_matrix[:, :, 2]))

        err = (abs(R_pic-R_tar), abs(G_pic - G_tar), abs(B_pic - B_tar))

        # TODO: Wymyslec, w jaki sposob normalizowac bledy
        return err

    @staticmethod
    def rgba_to_rgb(rgba_map): #nie używać
        img = Image.fromarray(rgba_map)
        img = img.convert('RGB')
        return np.asarray(img)

