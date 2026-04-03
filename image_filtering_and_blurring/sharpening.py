"""
Image Sharpening in OpenCV.

This script demonstrates how to enhance image edges using a mathematical 
convolution kernel with the cv2.filter2D function.
"""
import cv2
import numpy as np

# Load the original continuous tone image for edge enhancement
image = cv2.imread("assets/nature.jpg")

# Define a sharpening kernel (a matrix for mathematical convolution)
# The central value is positive, whereas surrounding values are negative
sharpen_kernal = np.array([
    [0, -1, 0],
    [-1, 5.1, -1],
    [0, -1, 0]
])

# Use cv2.filter2D() to apply the custom kernel to our image
# -1 indicates the output image will have the same depth as the source
sharpened = cv2.filter2D(image, -1, sharpen_kernal)

# Display the original and the sharpened image side-by-side
cv2.imshow("Original image", image)
cv2.imshow("Sharpened image", sharpened)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()