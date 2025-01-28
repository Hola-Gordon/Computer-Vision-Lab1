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
    num_cells_h, num_cells_w = grid.shape[:2]
    
    # Calculate cell dimensions
    cell_h = output_shape[0] // num_cells_h
    cell_w = output_shape[1] // num_cells_w
    
    # Initialize output array with exact output shape
    mosaic = np.zeros((output_shape[0], output_shape[1], 3), dtype=np.uint8)
    
    for i in range(num_cells_h):
        for j in range(num_cells_w):
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
            
            # Ensure tile exactly matches cell size
            tile = Image.fromarray(tile_images[best_tile_idx])
            tile = tile.resize((cell_w, cell_h), Image.LANCZOS)
            tile = np.array(tile)
            
            # Place tile in mosaic
            y_start = i * cell_h
            y_end = min((i + 1) * cell_h, output_shape[0])
            x_start = j * cell_w
            x_end = min((j + 1) * cell_w, output_shape[1])
            
            mosaic[y_start:y_end, x_start:x_end] = tile[:(y_end-y_start), :(x_end-x_start)]
    
    return mosaic