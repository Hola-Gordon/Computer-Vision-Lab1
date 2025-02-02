import os
import numpy as np
from PIL import Image


def load_tiles(tile_folder="assets", grid_size=8): 
    """
    Loads tiles and resizes them to match grid_size exactly
    """
    tiles = []
    if not os.path.exists(tile_folder):
        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        for color in colors:
            tile = np.full((grid_size, grid_size, 3), color, dtype=np.uint8)
            tiles.append(tile)
    else:
        for filename in os.listdir(tile_folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                try:
                    img = Image.open(os.path.join(tile_folder, filename))
                    img = img.convert("RGB")
                    img = img.resize((grid_size, grid_size), Image.NEAREST)
                    tiles.append(np.array(img))
                except Exception as e:
                    print(f"Error loading tile {filename}: {e}")
    return tiles


def generate_mosaic(image_array, grid_size):
    """
    Generates mosaic by replacing grid cells with best matching tiles
    """
    
    tiles = load_tiles(grid_size=grid_size)  
    if not tiles:
        raise ValueError("No tiles found in assets folder!")
        
    h, w = image_array.shape[:2]
    grid_h = h // grid_size
    grid_w = w // grid_size
    
    output = np.zeros_like(image_array)
    
    for i in range(grid_h):
        for j in range(grid_w):
            y1, y2 = i * grid_size, (i + 1) * grid_size
            x1, x2 = j * grid_size, (j + 1) * grid_size
            
            cell = image_array[y1:y2, x1:x2]
            best_tile = find_best_tile(cell, tiles)
            output[y1:y2, x1:x2] = best_tile
    
    return output


def find_best_tile(cell, tiles):
    """
    Finds the best matching tile for a given cell based on average color
    """
    cell_avg = np.mean(cell, axis=(0,1))
    
    best_tile_idx = 0
    min_diff = float('inf')
    
    for idx, tile in enumerate(tiles):
        tile_avg = np.mean(tile, axis=(0,1))
        diff = np.sum((cell_avg - tile_avg) ** 2)
        if diff < min_diff:
            min_diff = diff
            best_tile_idx = idx
            
    return tiles[best_tile_idx]

