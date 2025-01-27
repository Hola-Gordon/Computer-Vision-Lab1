import gradio as gr
from PIL import Image
import numpy as np
from src.image_processing import preprocess_image
from src.grid_operations import divide_into_grid
from src.tile_mapping import generate_mosaic, load_tiles


def mosaic_pipeline(image, grid_size=16):
    """
    Main pipeline for generating the mosaic.
    """
    # Store original size before preprocessing
    original_size = image.shape[:2] 
    # Preprocess the image
    processed_image = preprocess_image(image, target_size=(512, 512))
    
    # Divide into grid and get output dimensions
    grid = divide_into_grid(processed_image, grid_size)
    
    # Load tiles
    tile_images = load_tiles("assets", grid_size)
    
    # Generate mosaic
    mosaic_image = generate_mosaic(grid, tile_images, processed_image.shape)

    # Resize mosaic back to original size
    mosaic_image = Image.fromarray(mosaic_image)
    mosaic_image = mosaic_image.resize((original_size[1], original_size[0]))  # PIL uses (width, height)
    mosaic_image = np.array(mosaic_image)
    
    return mosaic_image


# Create Gradio interface
iface = gr.Interface(
    fn=mosaic_pipeline,
    inputs=[
        gr.Image(label="Upload Image", type="numpy"),
        gr.Slider(minimum=4, maximum=64, step=4, value=16, label="Grid Size")
    ],
    outputs=gr.Image(label="Mosaic Output"),
    title="Image Mosaic Generator",
    description="Upload an image and adjust the grid size to create a mosaic effect."
)

if __name__ == "__main__":
    iface.launch()
