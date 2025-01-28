from PIL import Image
import numpy as np

def preprocess_image(image, target_size=(512, 512), apply_quantization=False, num_colors=16):
    """
    Preprocesses the image while maintaining aspect ratio.
    """
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    # Adjust target size to maintain aspect ratio
    target_ratio = target_size[0] / target_size[1]
    img_ratio = image.size[0] / image.size[1]
    
    if img_ratio > target_ratio:
        # Width is the limiting factor
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
    else:
        # Height is the limiting factor
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
    
    # Resize and center crop to target size
    image = image.resize((new_width, new_height), Image.LANCZOS)
    left = (new_width - target_size[0]) // 2
    top = (new_height - target_size[1]) // 2
    right = left + target_size[0]
    bottom = top + target_size[1]
    image = image.crop((left, top, right, bottom))
    
    return np.array(image)
