import gradio as gr
from PIL import Image
import numpy as np
import os
from src.image_processing import preprocess_image
from src.grid_operations import divide_into_grid
from src.tile_mapping import generate_mosaic
from src.metrics import evaluate_mosaic


def mosaic_pipeline(image, grid_size=16):
    """
    Main pipeline for mosaic generation
    """
    # Preprocess image
    processed_image = preprocess_image(image)
    
    # Generate mosaic
    mosaic = generate_mosaic(processed_image, grid_size)
    
    # Calculate similarity metric
    metrics = evaluate_mosaic(processed_image, mosaic)
    print(f"MSE: {metrics['mse']:.2f}")
    print(f"SSIM: {metrics['ssim']:.3f}")
    print(f"PSNR: {metrics['psnr']:.2f} dB")
    
    # Create downloadable output
    output_image = Image.fromarray(mosaic)
    temp_path = "temp_mosaic.png"
    output_image.save(temp_path)
    
    return output_image, temp_path


# Create Gradio interface
iface = gr.Interface(
    fn=mosaic_pipeline,
    inputs=[
        gr.Image(label="Upload Image", type="pil"),
        gr.Slider(minimum=8, maximum=64, step=8, value=16, label="Grid Size")
    ],
    outputs=[
        gr.Image(label="Mosaic Output"),
        gr.File(label="Download Mosaic")
    ],
    title="Image Mosaic Generator",
    description="Upload an image to create a mosaic effect. Grid size must be a multiple of 8.",
    examples=[
        ["examples/coffee.jpg", 16],  
        ["examples/lake.jpg", 8],  
    ]
)

if __name__ == "__main__":
    iface.launch()