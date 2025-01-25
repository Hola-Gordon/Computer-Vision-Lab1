from PIL import Image
import numpy as np


def preprocess_image(image, target_size=(256, 256)):

    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)  # Convert NumPy to PIL if needed

    image = image.resize(target_size)  # Resize to fixed resolution
    return np.array(image)  # Convert back to NumPy array