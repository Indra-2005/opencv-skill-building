"""
Shape Detection in OpenCV.

This script demonstrates how to approximate contours to polygons 
and identify primitive geometric shapes based on their number of vertices.
"""
import cv2

# Load the image
img = cv2.imread("assets/triangle.jpg")

# Convert the image to grayscale, which is easier for thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to isolate the shapes
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find all contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the total image area to exclude overly small algorithms or the background itself
img_area = img.shape[0] * img.shape[1]

for contour in contours:
    # Calculate the area of the current contour
    area = cv2.contourArea(contour)
    
    # Filter out small noise and the bounding box of the entire image
    if area < 500 or area > 0.9 * img_area:
        continue
        
    # Approximate the contour to a polygon
    # The second parameter specifies the approximation accuracy
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # Determine the shape based on the number of corners (vertices) found
    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"
    
    # Draw the approximated polygon on the original image
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    
    # Compute the bounding rectangle to place the label neatly
    x, y, w, h = cv2.boundingRect(approx)
    
    # Adjust y-coordinate for the text to avoid rendering outside the top border
    text_y = y - 10 if y > 20 else y + 30
    
    # Overlay the identified shape name
    cv2.putText(img, shape_name, (x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)

# Display the final image with shape annotations
cv2.imshow("Shapes", img)

# Pause execution until a key is pressed
cv2.waitKey(0)

# Destroys all open UI windows
cv2.destroyAllWindows()