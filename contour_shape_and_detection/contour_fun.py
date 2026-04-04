"""
Contour Detection in OpenCV.

This script demonstrates how to find and draw contours on an image. 
Contours are continuous lines or curves that bound or cover the full boundary of an object.
"""
import cv2

# Load the image
img = cv2.imread("assets/triangle.jpg")

# Convert the image to grayscale, which is easier for thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to isolate the shapes
# Pixels above 200 become 255 (white), others become 0 (black)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
# RETR_TREE retrieves all contours and creates a full family hierarchy list
# CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
# -1 signifies drawing all found contours
# (0, 255, 0) specifies the color green with a line thickness of 3
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Display the resulting image with drawn contours
cv2.imshow("Contours", img)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()