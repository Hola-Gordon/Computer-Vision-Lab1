This is the README file
This is the README file
# Image Mosaic Generator

## Overview
The Image Mosaic Generator is a Python application designed to transform standard images into mosaic patterns. By dividing an image into grid cells of specified sizes and replacing each cell with a closely matching tile, the application creates a visually appealing mosaic effect. This project incorporates several performance metrics such as Mean Squared Error (MSE), Structural Similarity Index (SSIM), and Peak Signal-to-Noise Ratio (PSNR) to evaluate the fidelity of the mosaic to the original image.

## Features
- **Image Preprocessing**: Adjusts images to suitable sizes.
- **Mosaic Generation**: Converts processed images into mosaics using predefined tile sets.
- **Performance Evaluation**: Utilizes MSE, SSIM, and PSNR metrics for quality assessment.
- **Gradio Web Interface**: Provides an interactive web interface for easy usage of the mosaic generator.

## Installation

### Requirements
- Python 3.8 or later
- NumPy
- Pillow
- scikit-image
- Gradio

To install the required Python packages, run the following command:

```bash
pip install numpy pillow scikit-image gradio


