import torch
import torch.nn.functional as F

class SimpleBatch10Node:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # The first image determines the target dimensions for the batch
                "image1": ("IMAGE",),
            },
            "optional": {
                "image2": ("IMAGE",),
                "image3": ("IMAGE",),
                "image4": ("IMAGE",),
                "image5": ("IMAGE",),
                "image6": ("IMAGE",),
                "image7": ("IMAGE",),
                "image8": ("IMAGE",),
                "image9": ("IMAGE",),
                "image10": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("batch_image",)
    FUNCTION = "batch_images"
    CATEGORY = "My Tools/Image"

    def batch_images(self, image1, image2=None, image3=None, image4=None, image5=None, 
                     image6=None, image7=None, image8=None, image9=None, image10=None):
        
        # 1. Initialize the batch with the first image
        # image1 serves as the reference for dimensions (Height, Width)
        batch = image1
        target_h = image1.shape[1]
        target_w = image1.shape[2]

        # 2. Create a list of potential optional images
        other_images = [image2, image3, image4, image5, image6, image7, image8, image9, image10]
        
        # 3. Iterate through optional images
        for img in other_images:
            if img is not None:
                # Check if dimensions match the reference image
                if img.shape[1] != target_h or img.shape[2] != target_w:
                    # If dimensions differ, perform bilinear interpolation
                    # ComfyUI images are [Batch, Height, Width, Channel]
                    # torch.nn.functional.interpolate expects [Batch, Channel, Height, Width]
                    img = img.movedim(-1, 1)
                    img = F.interpolate(img, size=(target_h, target_w), mode="bilinear", align_corners=False)
                    img = img.movedim(1, -1)
                
                # Concatenate the processed image to the batch along the batch dimension (dim 0)
                batch = torch.cat((batch, img), dim=0)

        return (batch,)

# Node registration
NODE_CLASS_MAPPINGS = {
    "SimpleBatch10Node": SimpleBatch10Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleBatch10Node": "Batch 10 Images (Auto-Resize)"
}
