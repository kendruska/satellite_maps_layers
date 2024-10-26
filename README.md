# Satellite Image Processor

This project is a Python script for processing satellite images, generating different color layers, and visualizing the original and processed images. It also includes a 3D visualization of the elevation data from satellite imagery. This tool is particularly useful for analyzing satellite data for research, environmental monitoring, and geographic analysis.

## Features

- **Read satellite images**: The script reads satellite images in TIFF format, supporting up to 3 bands. This allows for processing images with multiple channels such as RGB or other combinations of spectral data.
- **Generate color-coded layers**: Based on pixel values, the script generates several color-coded layers that represent different ranges of values. These layers help visually identify various features in the landscape, such as vegetation, soil, or elevation differences.
- **Water layer representation**: The script includes a water layer, represented in a light blue color, which helps visually identify bodies of water in the satellite image.
- **Save processed layers**: All generated layers are saved as PNG files in the specified output folder, making it easy to analyze and share the processed data.
- **Visualization of images**: The script provides visualizations of both the original and processed images, including a side-by-side comparison of the original image and the processed water layer.
- **3D visualization**: The script includes a 3D view of the first band of the satellite image, which is useful for visualizing elevation data or other continuous surface information.

## Requirements

The following Python packages are required to run the script:

- `numpy`: For numerical operations, including processing and normalizing the image data.
- `rasterio`: For reading satellite image files in TIFF format.
- `opencv-python`: For saving the processed layers as images in PNG format.
- `matplotlib`: For visualizing the original and processed images, as well as creating 3D plots.

You can install these dependencies using `pip`:

```sh
pip install numpy rasterio opencv-python matplotlib
```

## Usage

To use the Satellite Image Processor, you need to provide a satellite image in TIFF format, specify an output folder for the generated images, and optionally set a water level threshold.

### Running the script

To run the script, use the following command:

```sh
python satellite_image_processor.py
```

By default, the script will look for a file named `test.tiff` in the current directory and will save the output in a folder named `output`. You can modify these defaults by passing command-line arguments or editing the script directly for more flexibility. You can modify the file path and output folder by editing the script or passing different parameters.

### Example Workflow

1. **Prepare the satellite image**: Ensure you have a TIFF image file (`test.tiff`) in the current directory. This image should contain up to 3 bands (e.g., RGB channels).
2. **Run the script**: Execute the script using the command mentioned above. The script will read the image, generate the color-coded layers, and save the results.
3. **View the results**: The processed images will be saved in the `output` folder. You will find individual PNG files for each layer, as well as a water layer representation.
4. **Visualize**: The script also provides visualizations, including a 3D plot of the first band and side-by-side comparisons of the original and processed images.

## Code overview

The main script is implemented in a single Python file named `satellite_image_processor.py`. The core functionality is encapsulated in the `SatelliteImageProcessor` class, which contains methods for reading, processing, saving, and visualizing satellite images.

### Class and methods

- **`SatelliteImageProcessor`**: Main class for processing satellite images.
  - **`__init__(file_path, output_folder, water_level)`**: Initializes the processor with the file path, output folder, and an optional water level parameter.
  - **`read_satellite_image()`**: Reads the satellite image from the specified file path and returns it as a NumPy array. Supports reading up to 3 bands from the image.
  - **`generate_image_layers()`**: Generates several color-coded layers based on the pixel values of the image. The colors represent different ranges of pixel intensity, allowing easy identification of different landscape features.
  - **`save_image_layers(layers, water_layer)`**: Saves the generated image layers and the water layer as PNG files in the specified output folder.
  - **`plot_3d_image()`**: Creates a 3D plot of the first band of the satellite image, providing a visualization that can be useful for interpreting elevation data or other spatial variations.
  - **`plot_original_image()`**: Plots the original satellite image to provide a baseline for comparison with the processed layers.
  - **`plot_processed_image(water_layer)`**: Plots the processed water layer to visualize areas identified as water bodies.
  - **`process()`**: Orchestrates the entire workflow, including reading the image, generating layers, saving outputs, and visualizing the results.

## Files

- **`satellite_image_processor.py`**: The main script that contains the `SatelliteImageProcessor` class and the code necessary to execute the image processing workflow.

## Output

The script produces the following output files in the specified output folder. These files can be used for further analysis, such as integrating into GIS tools for mapping, conducting spatial analysis, or sharing processed data for environmental and geographical studies:

- **Color-coded layers**: Several PNG files (`layer_0.png`, `layer_1.png`, etc.) representing different features in the satellite image based on pixel intensity.
- **Water layer**: A PNG file (`water_layer.png`) representing the detected water bodies in the image.

## Applications

This script can be used for various applications, including:

- **Environmental monitoring**: Identifying vegetation, water bodies, and other landscape features for environmental analysis.
- **Geographical analysis**: Creating visual representations of terrain and elevation data for geographic studies.
- **Disaster management**: Analyzing satellite images to identify flood zones or affected areas after natural disasters.
- **Agriculture**: Monitoring crop health, irrigation patterns, and other agricultural features using spectral data from satellite images.

## Customization

The script is designed to be easily customizable. Users can:

- **Modify color schemes**: Adjust the colors used for different pixel value ranges in the `generate_image_layers` method to suit specific applications.
- **Change water level threshold**: Modify the `water_level` parameter to set different thresholds for identifying water bodies.
- **Adapt image bands**: Update the `read_satellite_image` method to read more or fewer bands depending on the satellite data available.

## License

This project is licensed under the MIT License, allowing for open use, modification, and distribution.

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub. Whether it's optimizing the code, adding new features, or improving the documentation, all contributions are appreciated.

## Contact

If you have any questions or need further assistance, you can reach out via email or create an issue on the project's GitHub repository.



