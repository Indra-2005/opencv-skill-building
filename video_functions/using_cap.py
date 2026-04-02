"""
Capture a Live Video Feed using OpenCV.

This script demonstrates the basics of streaming a live webcam feed
using the cv2.VideoCapture class.

"""
import cv2

# Initialize the webcam capture (device 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Detect if the frame could not be read
    if not ret:
        print("Could not read frame")
        break
        
    # Display the frame in a window
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit the live feed
    if cv2.waitKey(1) & 0xff == ord('q'):
        print("Quitting....")
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
