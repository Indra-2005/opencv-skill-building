"""
Adding Text on an Image using OpenCV.

This script demonstrates how to overlay custom textual information
on an existing image using the OpenCV cv2.putText() function.
It also shows how to select specific font faces like FONT_HERSHEY_SIMPLEX.


"""
import cv2

# Load the image from the assets folder
image = cv2.imread("assets/DB.jpg")

# Check if the image was successfully loaded
if image is None:
    print("Oops! Your image is not working")
else:
    print("Image loaded successfully!")

    # Add text over the image
    # Syntax: cv2.putText(image, text, bottom_left_corner, font_face, font_scale, color (BGR), thickness)
    cv2.putText(image, "Pandaaa!", (150,400), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    
    # Display the result
    cv2.imshow("Adding text over image", image)
    
    # Wait indefinitely until a key is pressed, then close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()