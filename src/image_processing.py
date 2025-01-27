from PIL import Image
import numpy as np

def preprocess_image(image, target_size=(512, 512), apply_quantization=False, num_colors=16):
    """
    Preprocesses the image while maintaining aspect ratio.
    """
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    # Calculate new dimensions preserving aspect ratio
    aspect_ratio = image.size[0] / image.size[1]
    if aspect_ratio > 1:
        new_width = target_size[0]
        new_height = int(target_size[0] / aspect_ratio)
    else:
        new_height = target_size[1]
        new_width = int(target_size[1] * aspect_ratio)
    
    # Resize image
    image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # Convert to RGB and apply quantization if needed
    image = image.convert("RGB")
    if apply_quantization:
        image = image.convert("P", palette=Image.ADAPTIVE, colors=num_colors)
        image = image.convert("RGB")
    
    return np.array(image)
