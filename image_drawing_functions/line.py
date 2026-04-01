"""
Draw a Line on an Image using OpenCV.

This script demonstrates how to load an image, draw a straight line 
between two specified coordinates (pt1, pt2), and display the result.

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

    # Define line properties
    pt1 = (100, 150)       # Starting coordinate (x, y)
    pt2 = (300, 150)       # Ending coordinate (x, y)
    color = (255, 0, 0)    # Color of the line (B, G, R) -> Blue
    thickness = 4          # Thickness of the line in pixels

    # Draw the line on the image (modifies the object in place)
    # The function returns the modified image as well.
    line_image = cv2.line(image, pt1, pt2, color, thickness)

    # Save output for README demonstration
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_line.jpg"), line_image)

    # Display the result
    cv2.imshow("Line Image", line_image)
    
    # Wait for any key press before closing the windows
    print("Press any key in the image window to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()