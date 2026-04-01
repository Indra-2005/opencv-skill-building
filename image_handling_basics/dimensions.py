"""
Extracting Image Dimensions using OpenCV.

Images are loaded as NumPy arrays. We can access their structural properties 
such as Height, Width, and Number of Channels using the `.shape` attribute.
"""
import cv2
import os

# Configure the path to the sample image
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

# Load the image
image = cv2.imread(image_path)

if image is not None:
    # Extract dimensions using the .shape property of the NumPy array
    # h = height (rows)
    # w = width (columns)
    # c = channels (colors, usually 3 for BGR standard in OpenCV)
    h, w, c = image.shape
    
    print("Image Loaded Successfully!\n")
    print("--- Image Dimensions Properties ---")
    print(f" Height   = {h} pixels")
    print(f" Width    = {w} pixels")
    print(f" Channels = {c} (BGR)")
    print("-----------------------------------")
    
    # Save a text output of dimensions into README outputs
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "output_dimensions.txt"), "w") as f:
        f.write(f"Height={h}, Width={w}, Channels={c}")
else:
    print("Error: Could not load image. Check the path.")