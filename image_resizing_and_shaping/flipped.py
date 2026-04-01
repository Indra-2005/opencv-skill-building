"""
Image Flipping Algorithms.

Demonstrates cv2.flip with different axis configurations to flip horizontally,
vertically, or cross-axis.
"""
import cv2
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image")
else:
    # cv2.flip parameters:
    # 1  = Flip along the y-axis (Horizontal)
    # 0  = Flip along the x-axis (Vertical)
    # -1 = Flip along both axes
    flipped_horizontally = cv2.flip(image, 1)
    flipped_vertically = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    # Save output for README
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_flip_h.jpg"), flipped_horizontally)
    cv2.imwrite(os.path.join(output_dir, "output_flip_v.jpg"), flipped_vertically)

    print("Images flipped! Rendering displays...")
    cv2.imshow("Original", image)
    cv2.imshow("Flipped Horizontally (1)", flipped_horizontally)
    cv2.imshow("Flipped Vertically (0)", flipped_vertically)
    cv2.imshow("Flipped Both Axes (-1)", flipped_both)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
