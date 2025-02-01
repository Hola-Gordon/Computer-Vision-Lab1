import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr


def calculate_mse(original, mosaic):
    """
    Calculate Mean Squared Error between original and mosaic
    Lower values indicate better similarity
    """
    return np.mean((original.astype(float) - mosaic.astype(float)) ** 2)


def calculate_ssim(original, mosaic):
    """
    Calculate Structural Similarity Index
    Values closer to 1 indicate better similarity
    """
    if len(original.shape) == 3:
        # Calculate SSIM for each color channel and take mean
        return np.mean([ssim(original[:,:,i], mosaic[:,:,i], data_range=255) 
                       for i in range(original.shape[2])])
    return ssim(original, mosaic, data_range=255)


def calculate_psnr(original, mosaic):
    """
    Calculate Peak Signal-to-Noise Ratio
    Higher values indicate better quality (measured in dB)
    """
    return psnr(original, mosaic, data_range=255)


def evaluate_mosaic(original, mosaic):
    """
    Evaluate mosaic quality using MSE, SSIM, and PSNR
    """
    return {
        'mse': calculate_mse(original, mosaic),
        'ssim': calculate_ssim(original, mosaic),
        'psnr': calculate_psnr(original, mosaic)
    }