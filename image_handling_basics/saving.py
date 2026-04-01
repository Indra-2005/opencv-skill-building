"""
Saving Images using OpenCV.

This script demonstrates how to save a modified image back to disk 
using cv2.imwrite.
"""
import cv2
import os

# Set target paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")
save_path = os.path.join(base_dir, "assets", "outputs", "output_saved.jpg")

os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Read the image
image = cv2.imread(image_path)

if image is not None:
    # Write the image to disk
    # This will create a copy of the image and return True if successful
    success = cv2.imwrite(save_path, image)
    
    if success:
        print(f"Image saved successfully to {save_path}")
    else:
        print("Error: Failed to save the image (check directory permissions).")
else:
    print("Error: Could not load the initial image.")