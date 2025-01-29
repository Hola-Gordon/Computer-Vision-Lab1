import numpy as np

def calculate_mse(original, mosaic):
    """
    Calculate Mean Squared Error between original and mosaic
    """
    return np.mean((original - mosaic) ** 2)