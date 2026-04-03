"""
Bitwise Operations in OpenCV.

This script demonstrates how to perform bitwise operations AND, OR, and NOT 
on binary and mask images.

* Images must have the same height and width.
* Best used on black and white (binary) masks.
"""

import cv2
import numpy as np


# Create two blank black images of the same dimensions (300x300)
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a filled white circle on the first image
cv2.circle(img1, (150, 150), 100, 255, -1)

# Draw a filled white rectangle on the second image
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

# Perform bitwise AND (Intersection: regions where BOTH are white)
bitwise_and = cv2.bitwise_and(img1, img2)

# Perform bitwise OR (Union: regions where EITHER is white)
bitwise_or = cv2.bitwise_or(img1, img2)

# Perform bitwise NOT (Inversion: flip white to black and vice versa)
bitwise_not = cv2.bitwise_not(img1)


# Display all resulting combinations
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()