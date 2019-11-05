import numpy as np


class ImageHelper:

    def convert_image_into_array(image):
        pixel_vals = list(image.getdata())
        n, _ = image.size
        new_list = []
        for i in range(0, len(pixel_vals), n):
            new_list.append(pixel_vals[i:i + n])
        return new_list

