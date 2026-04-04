"""
Basic Face Detection using OpenCV's Haar Cascade Classifiers.

Demonstrates loading a pre-trained face detection model and applying it
to a live webcam feed to draw bounding boxes around detected faces.
"""
import cv2

# Load the pre-trained Haar Cascade classifier for frontal face detection.
# This XML file contains the statistical features of a face.
face_cascade = cv2.CascadeClassifier(r"face_and_object_detection\haarcascade_frontalface_default.xml")

# Open the default webcam (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale since Haar cascades operate on grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image.
    # detectMultiScale parameters:
    # - scaleFactor (1.1): How much the image size is reduced at each image scale
    # - minNeighbors (5): Minimum number of neighbor rectangles needed to retain a detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # faces returns an array of rects (x, y, w, h)
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        # (x, y) forms the top-left corner
        # (x+w, y+h) forms the bottom-right corner
        # (255, 255, 255) is the color (White), and 2 is the thickness
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

    # Display the processed frame
    cv2.imshow("Webcam Face Detection", frame)
    
    # Break out of the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all active windows
cap.release()
cv2.destroyAllWindows()
