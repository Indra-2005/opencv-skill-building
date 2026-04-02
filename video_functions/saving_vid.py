"""
Capture and Save a Video using OpenCV.

This script demonstrates how to capture live video from a webcam,
display it, and continuously save frames to an AVI video file.

"""
import cv2

# Initialize the webcam capture (device 0)
cam = cv2.VideoCapture(0)

# Get the default frame width and height from the camera
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec (XVID) and create VideoWriter object
codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("My_video.avi", codec, 20.0, (frame_width, frame_height))

while True:
    # Read a frame from the webcam
    success, image = cam.read()

    # Break if frame reading fails
    if not success:
        break

    # Write the frame into the file 'My_video.avi'
    recorder.write(image)
    
    # Show the live feed
    cv2.imshow("Recording live", image)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the camera and writer, then close windows
cam.release()
recorder.release()
cv2.destroyAllWindows()