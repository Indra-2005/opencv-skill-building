"""
Image Resizing without breaking Aspect Ratios.

Demonstrates how to manually define a target size structure to downscale 
or upscale an image properly using cv2.resize().
"""
import cv2
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")

    # cv2.resize takes the image and a tuple of the destination size (width, height)
    # Notice: width is given before height here, opposite of normal image[h, w] arrays!
    resized = cv2.resize(image, (300, 300))

    # Save outputs for README
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_imresize.jpg"), resized)

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image (300x300)", resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()