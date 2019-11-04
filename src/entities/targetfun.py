import numpy as np
from PIL import Image


class TargetFunction:

    @staticmethod
    def create_target(image):
        arr = np.asarray(image)
        return arr

    @staticmethod
    def calculate_error(pic_matrix, target_matrix):
        sub = np.subtract(pic_matrix, target_matrix)
        (raw_errR, raw_errG, raw_errB) = (np.sum(sub[0, :, :]), np.sum(sub[1, :, :]),
                                          np.sum(sub[2, :, :]))
        # TODO: Wymyslec, w jaki sposob normalizowac bledy
        return raw_errR, raw_errG, raw_errB

    @staticmethod
    def rgba_to_rgb(rgba_map):
        img = Image.fromarray(rgba_map)
        img = img.convert('RGB')
        return np.asarray(img)

