import numpy as np


def divide_into_grid(image, grid_size):

    h, w, c = image.shape
    grid_h, grid_w = h // grid_size, w // grid_size  # Number of rows & columns

    # Reshape the image into a 5D array: (grid_h, grid_w, grid_size, grid_size, C)
    grid = image.reshape(grid_h, grid_size, grid_w, grid_size, c)

    # Compute number of rows and columns
    grid_h, grid_w = h // grid_size, w // grid_size

    # Reshape image into grid blocks
    grid = image.reshape(grid_h, grid_size, grid_w, grid_size, c)

    # Rearrange axes (rows, cols, height, width, channels)
    grid = np.moveaxis(grid, [1, 2], [2, 3])

    return grid