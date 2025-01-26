from src.image_processing import preprocess_image
from src.grid_operations import divide_into_grid
from src.tile_mapping import generate_mosaic, load_tiles
import gradio as gr
from PIL import Image



def mosaic_pipeline(image, grid_size=16):
    """
    Generates a tile-based mosaic from an input image.

    Args:
        image (PIL Image or NumPy array): Input image.
        grid_size (int): Grid size for dividing the image.

    Returns:
        numpy array: Reconstructed mosaic using tile images.
    """
    processed_image = preprocess_image(image, target_size=(256, 256), apply_quantization=False, num_colors=16)
    original_shape = processed_image.shape[:2]  # Get (height, width)
    grid = divide_into_grid(processed_image, grid_size)

    # ✅ Load tiles dynamically with the selected grid size
    tile_images = load_tiles("assets", grid_size)

    mosaic_image = generate_mosaic(grid, tile_images, original_shape)  # Preserve shape

    return mosaic_image


# Gradio UI
iface = gr.Interface(
    fn=mosaic_pipeline,
    inputs=[
        gr.Image(label="Upload Image"),
        gr.Slider(4, 64, step=4, value=16, label="Grid Size"),
    ],
    outputs="image"
)

if __name__ == "__main__":
    iface.launch()
