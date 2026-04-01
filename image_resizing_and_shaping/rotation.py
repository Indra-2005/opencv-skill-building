"""
Rotating an Image with OpenCV.

To rotate an image, you must first define a standard rotation matrix.
cv2.getRotationMatrix2D provides a way to calculate this matrix.
"""
import cv2
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, "assets", "DB.jpg")

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Get image dimensions to find the exact center
    (h, w) = image.shape[:2]
    
    # Calculate the center of rotation
    center = (w // 2, h // 2)
    
    # Generate the 2D rotation matrix:
    # 1. Center of the image
    # 2. Angle of rotation (75 degrees counter-clockwise)
    # 3. Scaling factor (1.0 means same scale)
    M = cv2.getRotationMatrix2D(center, 75, 1.0)
    
    # Perform the actual affine transformation applying the matrix
    rotated = cv2.warpAffine(image, M, (w, h))

    # Save output for README demonstration
    output_dir = os.path.join(base_dir, "assets", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, "output_rotated.jpg"), rotated)

    print("Rotation Applied! Visualizing Result...")
    cv2.imshow("Original Input", image)
    cv2.imshow("Rotated Image (75 Degrees)", rotated)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()