import os
import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse

class SatelliteImageProcessor:
    def __init__(self, file_path, output_folder, water_level=0):
        self.file_path = file_path
        self.output_folder = output_folder
        self.water_level = water_level
        self.image = self.read_satellite_image()

    def read_satellite_image(self):
        with rasterio.open(self.file_path) as dataset:
            available_bands = dataset.count
            bands_to_read = [i for i in range(1, min(4, available_bands + 1))]  # Read up to 3 bands
            image = dataset.read(bands_to_read)
        return image

    def generate_image_layers(self):
        min_value = np.min(self.image)
        max_value = np.max(self.image)
        
        colors = [
            (173, 255, 47),  # Light yellow-green
            (154, 205, 50),   # Darker green
            (107, 142, 35),   # Dark olive green
            (85, 107, 47),    # Darker olive green
            (139, 69, 19),    # Dark brown
            (160, 82, 45),    # Light reddish-brown
            (210, 105, 30),   # Orange-brown
            (244, 164, 96),   # Light brown
            (165, 42, 42)     # Dark reddish-brown
        ]

        normalized_image = (self.image - min_value) / (max_value - min_value)

        layers = []
        for i, color in enumerate(colors):
            threshold = (i + 1) / 10.0
            layer = np.where(normalized_image[0] >= threshold, 255 * (i + 1) / 10, 0).astype(np.uint8)
            layer_colored = np.zeros((layer.shape[0], layer.shape[1], 3), dtype=np.uint8)
            for j in range(3):
                layer_colored[:, :, j] = layer * (color[j] / 255)
            layers.append(layer_colored)

        # Create water layer with light blue color (RGB: 135, 206, 235)
        water_layer_colored = np.zeros((self.image.shape[1], self.image.shape[2], 3), dtype=np.uint8)
        water_layer_colored[:, :, 0] = 135  # Red channel
        water_layer_colored[:, :, 1] = 206  # Green channel
        water_layer_colored[:, :, 2] = 235  # Blue channel

        return layers, water_layer_colored

    def save_image_layers(self, layers, water_layer):
        os.makedirs(self.output_folder, exist_ok=True)

        for i, layer in enumerate(layers):
            cv2.imwrite(f"{self.output_folder}/layer_{i}.png", cv2.cvtColor(layer, cv2.COLOR_RGB2BGR))

        cv2.imwrite(f"{self.output_folder}/water_layer.png", cv2.cvtColor(water_layer, cv2.COLOR_RGB2BGR))

    def plot_3d_image(self):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        X, Y = np.meshgrid(np.arange(self.image.shape[2]), np.arange(self.image.shape[1]))
        ax.plot_surface(X, Y, self.image[0], cmap='terrain', edgecolor='none')
        ax.set_title('3D View of the Satellite Image')
        plt.show()

    def plot_original_image(self):
        if self.image.shape[0] == 1:
            img_to_plot = np.repeat(self.image[0, :, :][..., np.newaxis], 3, axis=2)
        elif self.image.shape[0] == 2:
            img_to_plot = np.concatenate([self.image[0:2], self.image[0:1]], axis=0)  # Repeat the first channel
            img_to_plot = np.transpose(img_to_plot, (1, 2, 0))
        elif self.image.shape[0] >= 3:
            img_to_plot = np.transpose(self.image[:3], (1, 2, 0))  # Take the first 3 bands

        plt.imshow(img_to_plot)
        plt.title('Original Satellite Image')
        plt.show()

    def plot_processed_image(self, water_layer):
        plt.imshow(water_layer)
        plt.title('Water Layer Image')
        plt.show()

    def process(self):
        layers, water_layer = self.generate_image_layers()
        self.save_image_layers(layers, water_layer)

        # Plot original image and water layer
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))

        if self.image.shape[0] >= 3:
            original_image = np.transpose(self.image[:3], (1, 2, 0))
        else:
            original_image = self.image[0]

        original_image = (original_image - original_image.min()) / (original_image.max() - original_image.min())
        original_image = (original_image * 255).astype(np.uint8)

        axs[0].imshow(original_image if original_image.ndim == 3 else np.stack([original_image] * 3, axis=-1))
        axs[0].set_title('Original Satellite Image')

        axs[1].imshow(water_layer)
        axs[1].set_title('Processed Water Layer')

        plt.show()

        # Show 3D plot of the first band
        self.plot_3d_image()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a satellite image and generate different layers.")
    parser.add_argument("file_path", type=str, help="Path to the input satellite image file (e.g., .tiff file)")
    parser.add_argument("output_folder", type=str, help="Path to the output folder to save processed images")
    parser.add_argument("--water_level", type=float, default=0, help="Water level threshold (default: 0)")

    args = parser.parse_args()

    processor = SatelliteImageProcessor(file_path=args.file_path, output_folder=args.output_folder, water_level=args.water_level)
    processor.process()
