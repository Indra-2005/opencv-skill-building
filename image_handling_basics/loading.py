"""
Basic Image Loading in OpenCV.

This script demonstrates the foundational step in Computer Vision:
Reading an image from the disk and displaying it in a window using OpenCV.
"""
import cv2
import os

# Create an absolute path to the assets directory automatically
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

# cv2.imread reads the image as a NumPy array.
# By default, it reads in BGR (Blue, Green, Red) format.
image = cv2.imread(image_path)

if image is not None:
    print("Successfully loaded image.")
    # Show the image window
    cv2.imshow("Original Image Frame", image)
    
    # Save a generic output copy for README
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_loaded.jpg"), image)

    # cv2.waitKey(0) pauses the execution indefinitely until a key is pressed.
    print("Press any key to close the visualization...")
    cv2.waitKey(0) 
    
    # Destroys all open UI windows created by cv2
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not load the image from {image_path}")
