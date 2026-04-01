"""
Image Cropping using OpenCV and NumPy arrays.

Because an image is just an N-dimensional array (NumPy array), you can crop it 
simply by using standard Python slicing (Array Slicing) - [row_range, col_range].
"""
import cv2
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

image = cv2.imread(image_path)

if image is not None:
    # Cropping syntax: image[y_start:y_end, x_start:x_end]
    # Remembering that the height is the first dimension!
    cropped = image[100:200, 50:150]
    
    # Save the output for demonstration
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_cropped.jpg"), cropped)

    print("Image cropped. Displaying original and cropped views.")
    cv2.imshow("Original Input", image)
    cv2.imshow("Cropped Image Segment", cropped)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Failed to load the image")