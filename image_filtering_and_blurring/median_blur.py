"""
Median Blurring in OpenCV.

This script demonstrates how to apply a Median blur filter.
Median blurring is exceptionally good at correcting "salt-and-pepper" noise
by replacing each pixel with the median of its neighboring pixels.
"""
import cv2

# Load the noisy image containing salt-and-pepper noise
image = cv2.imread("assets/noisy.jpg")

# Apply a Median Blur to the image
# Parameters: input image, kernel size (must be an odd integer)
blurred = cv2.medianBlur(image, 7)

# Display both the original and the cleaned image
cv2.imshow("Original (Noisy)", image)
cv2.imshow("Clean Image (Median Blur)", blurred)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()