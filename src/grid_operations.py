import numpy as np


def divide_into_grid(image, grid_size):
    """
    Divides image into a grid while preserving dimensions.
    """
    h, w, c = image.shape
    
    # Calculate number of cells, rounding up to include full image
    num_cells_h = int(np.ceil(h / grid_size))
    num_cells_w = int(np.ceil(w / grid_size))
    
    # Calculate padded size to fit all cells
    new_h = num_cells_h * grid_size
    new_w = num_cells_w * grid_size
    
    # Create padded image
    padded_image = np.zeros((new_h, new_w, c), dtype=image.dtype)
    padded_image[:h, :w] = image
    
    # Reshape into grid
    grid = padded_image.reshape(num_cells_h, grid_size, num_cells_w, grid_size, c)
    grid = grid.swapaxes(1, 2).reshape(num_cells_h, num_cells_w, grid_size, grid_size, c)
    
    return grid