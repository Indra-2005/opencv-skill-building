"""
Draw a Rectangle on an Image using OpenCV.

This script demonstrates how to load an image, draw a rectangle 
given top-left and bottom-right corners, and display the result.

Author: GitHub Contributor
"""
import cv2
import os

# Construct the path to the image in the assets folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

# Load the image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image at {image_path}")
else:
    print("Image loaded successfully!")

    # Define rectangle properties
    pt1 = (50, 50)         # Top-Left corner (x, y)
    pt2 = (250, 200)       # Bottom-Right corner (x, y)
    color = (0, 0, 255)    # Color of the rectangle border (B, G, R) -> Red
    thickness = 3          # Thickness of the border in pixels (-1 for filled)

    # Draw the rectangle
    cv2.rectangle(image, pt1, pt2, color, thickness)

    # Save output for README demonstration
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_rectangle.jpg"), image)

    # Display the result
    cv2.imshow("Image with Rectangle", image)
    print("Press any key to close the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()