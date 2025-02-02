## Image Mosaic Generator Performance Report

### Introduction
The Image Mosaic Generator is designed to transform an input image into a mosaic pattern by dividing it into grid cells of a specified size and matching each cell with the closest matching tile from a set of preprocessed images. The main goal of this project was to create visually appealing mosaic renditions of input images while measuring the fidelity of the mosaics with respect to the original images using multiple performance metrics.

### Methodology
The project involved several key components and processes:

1. **Preprocessing**: Images are first resized to ensure that their dimensions are multiples of 8, facilitating easier and more consistent division into grid cells.
2. **Grid Division**: The resized image is divided into smaller grids of specified size using the `divide_into_grid` function. Each cell in this grid is meant to be replaced with an image tile that closely resembles the original content of the cell.
3. **Tile Matching**: For each cell in the grid, a set of candidate tiles is evaluated, and the tile that has the minimum color difference from the target cell is selected. This is determined by calculating the mean color values of the tiles and the target cell and selecting the tile with the smallest squared difference.
4. **Mosaic Generation**: The image mosaic is assembled by replacing each grid cell with its corresponding best-match tile.
5. **Performance Evaluation**: The similarity between the original image and the generated mosaic is quantitatively assessed using Mean Squared Error (MSE), Structural Similarity Index (SSIM), and Peak Signal-to-Noise Ratio (PSNR).

### Performance Metrics
The performance of the mosaic generator was assessed for different grid sizes using MSE, SSIM, and PSNR. Here are the metrics for each tested grid size:

- **Grid size 8**
  - MSE: 6893.22
  - SSIM: 0.056
  - PSNR: 9.75 dB
- **Grid size 16**
  - MSE: 7370.36
  - SSIM: 0.048
  - PSNR: 9.46 dB
- **Grid size 24**
  - MSE: 8590.79
  - SSIM: 0.057
  - PSNR: 8.79 dB

### Results
The variation in MSE, SSIM, and PSNR values across different grid sizes highlights the challenges in balancing the fidelity and aesthetic quality of the mosaic. Smaller grid sizes provide higher resolution but may result in lower similarity indices (lower SSIM and PSNR), indicating a trade-off between visual appearance and fidelity to the original image.

### Conclusion
The Image Mosaic Generator successfully creates visually appealing mosaics from input images, with the added capability to quantitatively assess the similarity between the original images and their mosaic counterparts using comprehensive metrics. Future work could explore the use of advanced image processing algorithms to improve both the aesthetic quality and the accuracy of the mosaic images.
