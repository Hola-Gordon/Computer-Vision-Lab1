from PIL import Image
import numpy as np


def preprocess_image(image, target_size=(256, 256), apply_quantization=False, num_colors=16):
    """
    Resizes the input image to a fixed resolution while preserving its original aspect ratio.
    Optionally applies color quantization to simplify color variations.

    Args:
        image (PIL Image or NumPy array): The input image.
        target_size (tuple): The target (width, height) for resizing.
        apply_quantization (bool): Whether to apply color quantization.
        num_colors (int): Number of colors to quantize to.

    Returns:
        numpy array: Preprocessed image in NumPy format.
    """
    # Convert to PIL Image if needed
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)  

    # Ensure the image is in RGB mode
    image = image.convert("RGB")  

    # Resize to a fixed resolution
    image = image.resize(target_size, Image.LANCZOS)

    # Optional: Apply color quantization
    if apply_quantization:
        image = image.convert("P", palette=Image.ADAPTIVE, colors=num_colors)
        image = image.convert("RGB")  # Convert back to RGB after quantization

    return np.array(image)  # Always return NumPy array
