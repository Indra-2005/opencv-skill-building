"""
Image Thresholding in OpenCV.

This script demonstrates how to apply a simple binary threshold to an image,
converting grayscale or color intensities into a purely binary (black and white) image.
"""
import cv2

# Load the original image
image = cv2.imread("assets/Black_FL.jpg")

# Apply a binary threshold
# Parameters:
# 1. Source image
# 2. Threshold value (120 in this case)
# 3. Maximum value to assign if a pixel exceeds the threshold (255 - pure white)
# 4. Thresholding style (cv2.THRESH_BINARY)
ret, thresh_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

# Display the original and the thresholded image side-by-side
cv2.imshow("Original image", image)
cv2.imshow("Threshold image", thresh_img)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()