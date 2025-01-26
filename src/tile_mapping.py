import os
import numpy as np
from PIL import Image


def load_tiles(tile_folder, grid_size):
    """
    Loads all tile images from a folder and resizes them to `grid_size`.

    Args:
        tile_folder (str): Path to tile images.
        grid_size (int): The size of each tile (should match grid cells).

    Returns:
        list: List of resized tile images as NumPy arrays.
    """
    tiles = []
    for filename in os.listdir(tile_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(os.path.join(tile_folder, filename))
            img = img.resize((grid_size, grid_size))  # Resize to match grid size
            tiles.append(np.array(img))  # Convert to NumPy array
    return tiles


def closest_tile(cell, tile_images):
    """
    Finds the closest matching tile based on color similarity.

    Args:
        cell (numpy array): Image region (grid cell).
        tile_images (list): List of tile images.

    Returns:
        numpy array: Best-matching tile.
    """
    avg_color = cell.mean(axis=(0, 1))  # Compute average color of grid cell

    def color_distance(tile):
        return np.linalg.norm(tile.mean(axis=(0, 1)) - avg_color)

    best_tile = min(tile_images, key=color_distance)  # Find closest match
    return best_tile


def generate_mosaic(grid, tile_images, original_shape):
    """
    Converts each grid cell into a tile from the preloaded images while keeping original dimensions.

    Args:
        grid (numpy array): Grid of image cells.
        tile_images (list): List of tile images.
        original_shape (tuple): The original image's height and width.

    Returns:
        numpy array: Mosaic image with the same dimensions as the input.
    """
    h, w = len(grid), len(grid[0])
    orig_h, orig_w = original_shape[:2]  # Get original image size

    # Get tile size from first tile
    tile_h, tile_w = tile_images[0].shape[:2]

    # Create an empty mosaic canvas matching original size
    mosaic = np.zeros((orig_h, orig_w, 3), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            tile = closest_tile(grid[i][j], tile_images)  # Get best matching tile
            start_h, start_w = i * tile_h, j * tile_w
            end_h, end_w = start_h + tile_h, start_w + tile_w

            # Ensure we don't go beyond the original image bounds
            if end_h <= orig_h and end_w <= orig_w:
                mosaic[start_h:end_h, start_w:end_w] = tile

    return mosaic