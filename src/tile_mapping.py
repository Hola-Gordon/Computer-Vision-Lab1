import numpy as np
from PIL import Image
import os


def load_tiles(tile_folder, grid_size):
    """
    Loads and preprocesses tiles to match grid cell size.
    """
    tiles = []
    if not os.path.exists(tile_folder):
        # Create default colored tiles if no tiles exist
        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        for color in colors:
            tile = np.full((grid_size, grid_size, 3), color, dtype=np.uint8)
            tiles.append(tile)
    else:
        for filename in os.listdir(tile_folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                img = Image.open(os.path.join(tile_folder, filename))
                img = img.convert("RGB")
                img = img.resize((grid_size, grid_size))
                tiles.append(np.array(img))
    
    return tiles


def generate_mosaic(grid, tile_images, output_shape):
    """
    Generates mosaic while maintaining consistent dimensions.
    """
    grid_size = len(grid)
    cell_h = output_shape[0] // grid_size
    cell_w = output_shape[1] // grid_size
    
    # Initialize output array
    mosaic = np.zeros((output_shape[0], output_shape[1], 3), dtype=np.uint8)
    
    for i in range(grid_size):
        for j in range(grid_size):
            # Get average color of grid cell
            cell = grid[i, j]
            avg_color = np.mean(cell, axis=(0,1))
            
            # Find best matching tile
            best_tile_idx = 0
            min_diff = float('inf')
            for idx, tile in enumerate(tile_images):
                tile_avg = np.mean(tile, axis=(0,1))
                diff = np.sum((avg_color - tile_avg) ** 2)
                if diff < min_diff:
                    min_diff = diff
                    best_tile_idx = idx
            
            # Resize tile to match cell size
            tile = Image.fromarray(tile_images[best_tile_idx])
            tile = tile.resize((cell_w, cell_h))
            tile = np.array(tile)
            
            # Place tile in mosaic
            y_start = i * cell_h
            y_end = (i + 1) * cell_h
            x_start = j * cell_w
            x_end = (j + 1) * cell_w
            mosaic[y_start:y_end, x_start:x_end] = tile
    
    return mosaic