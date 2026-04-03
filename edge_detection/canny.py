"""
Canny Edge Detection in OpenCV.

This script demonstrates how to detect structural edges in an image using 
the Canny edge detection algorithm.
"""
import cv2 


# Load the image in grayscale, as edge detection works best on 1-channel images
image = cv2.imread("assets/Flower.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
# Parameters:
# 1. Source image
# 2. Lower threshold value: Gradient values below this are discarded.
# 3. Upper threshold value: Gradient values above this are considered sure edges.
edges = cv2.Canny(image, 50, 150)

# Display the original grayscale image and the resulting edges
cv2.imshow("Original image", image)
cv2.imshow("Edges image", edges)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()