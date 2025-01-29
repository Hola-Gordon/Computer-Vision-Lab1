import numpy as np


def divide_into_grid(image_array, grid_size):
    """
    Divides image into grid cells of specified size
    """
    h, w = image_array.shape[:2]
    grid_h = h // grid_size
    grid_w = w // grid_size
    
    return grid_h, grid_w