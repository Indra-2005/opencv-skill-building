"""
Gaussian Blurring in OpenCV.

This script demonstrates how to apply a Gaussian blur filter to an image.
Gaussian blurring is highly effective in removing Gaussian noise and softening image details.
"""
import cv2

# Load the original image from the assets folder
image = cv2.imread("assets/nature.jpg")

# Apply a Gaussian Blur to the image
# Parameters: input image, kernel size (must be odd), standard deviation in X
blurred = cv2.GaussianBlur(image, (7, 7), 3)

# Display the original and the blurred image
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()