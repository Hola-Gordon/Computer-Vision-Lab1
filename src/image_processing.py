from PIL import Image
import numpy as np


def resize_to_multiple_of_8(image):
    """
    Resizes image to have dimensions as multiples of 8
    """
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    w, h = image.size
    new_w = ((w + 7) // 8) * 8
    new_h = ((h + 7) // 8) * 8
    return image.resize((new_w, new_h))


def preprocess_image(image):
    """
    Basic image preprocessing
    """
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    # Resize to multiple of 8
    image = resize_to_multiple_of_8(image)
    return np.array(image)