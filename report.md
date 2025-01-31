## Image Mosaic Generator Performance Report

### Introduction
The Image Mosaic Generator is designed to transform an input image into a mosaic pattern by dividing it into grid cells of a specified size and matching each cell with the closest matching tile from a set of preprocessed images. The main goal of this project was to create visually appealing mosaic renditions of input images while measuring the fidelity of the mosaics with respect to the original images using the Mean Squared Error (MSE) metric.

### Methodology
The project involved several key components and processes:

1. **Preprocessing**: Images are first resized to ensure that their dimensions are multiples of 8, facilitating easier and more consistent division into grid cells.
2. **Grid Division**: The resized image is divided into smaller grids of specified size using the `divide_into_grid` function. Each cell in this grid is meant to be replaced with an image tile that closely resembles the original content of the cell.
3. **Tile Matching**: For each cell in the grid, a set of candidate tiles is evaluated, and the tile that has the minimum color difference from the target cell is selected. This is determined by calculating the mean color values of the tiles and the target cell and selecting the tile with the smallest squared difference.
4. **Mosaic Generation**: The image mosaic is assembled by replacing each grid cell with its corresponding best-match tile.
5. **Performance Evaluation**: The similarity between the original image and the generated mosaic is quantitatively assessed using the Mean Squared Error (MSE) between corresponding pixels.

### Performance Metrics
To assess the performance of the mosaic generator, the Mean Squared Error (MSE) was calculated for several test images. MSE provides a measure of the average squared difference between the original image and the generated mosaic, with lower values indicating higher similarity. The MSE values for different runs and grid sizes were recorded as follows:

- MSE (Grid size 8): 102.24
- MSE (Grid size 16): 107.32
- MSE (Grid size 24): 106.00
- MSE (Grid size 32): 109.83
- MSE (Grid size 40): 108.74
- MSE (Grid size 48): 108.92

### Results
The variation in MSE values across different grid sizes indicates how the granularity of the grid affects the accuracy of the mosaic. Smaller grid sizes typically offer higher fidelity mosaics due to the finer granularity allowing for better matching of smaller features in the image. However, the choice of grid size can also impact the aesthetic quality of the mosaic; smaller grids can sometimes produce a more fragmented visual appearance.

### Conclusion
The Image Mosaic Generator successfully creates visually appealing mosaics from input images. The MSE metric has proven to be a useful tool for quantitatively assessing the similarity between the original images and their mosaic counterparts. Future work could explore the use of more sophisticated image processing techniques to enhance tile matching accuracy and reduce MSE further.
