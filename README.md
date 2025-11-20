# ComfyUI Simple Batch Node

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows batching up to 10 images into a single batch tensor. 

It automatically resizes all input images to match the dimensions of the first image using bilinear interpolation, preventing dimension mismatch errors.

## Features

- **Batch up to 10 images**: Connect anywhere from 1 to 10 images.
- **Auto-Resize**: Automatically scales `image2` through `image10` to match the height and width of `image1`.
- **Native Behavior**: Uses the same logic as the native ComfyUI "Image Batch" node but with more inputs.

## Installation

### Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ComfyUI-SimpleBatch-Node.git](https://github.com/YOUR_USERNAME/ComfyUI-SimpleBatch-Node.git)
