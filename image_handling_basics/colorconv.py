"""
Image Color Conversion.

OpenCV allows converting images easily from one color space to another.
In this script, we convert the default BGR (Color) image into a Grayscale image.
"""
import cv2
import os

# Construct path to assets
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

image = cv2.imread(image_path)

if image is not None:
    # Convert BGR (OpenCV default) to GrayScale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    print("Image converted to grayscale successfully!")

    # Save output for README
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_gray.jpg"), gray)

    # Show the resulting Grayscale image
    cv2.imshow("Grayscale Image", gray)
    print("Press any key to exit...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Failed to load the image.")