"""
Draw a Circle on an Image using OpenCV.

This script demonstrates how to procedurally draw vector shapes (circles)
on top of raster image backgrounds using the OpenCV cv2.circle() function.


"""
import cv2

# Load the image from the assets folder
image = cv2.imread("assets/DB.jpg")

# Check if the image was successfully loaded
if image is None:
    print("Oops! Your image is not working.")
else:
    print("Image loaded successfully!")
    
    # Draw a circle on the image
    # Syntax: cv2.circle(image, center_coordinates, radius, color (BGR), thickness)
    # thickness=1 means a hollow circle with 1px border. Negative thickness would fill it.
    cv2.circle(image, (525, 150), 150, (255, 0, 0), 1)

    # Display the result
    cv2.imshow("Drawing Circle", image)
    
    # Wait indefinitely until a key is pressed, then close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()