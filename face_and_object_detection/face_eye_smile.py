"""
Advanced Haar Cascade Detection for OpenCV.

Demonstrates loading multiple pre-trained Haar Cascades to detect the bounding 
boxes for faces, and within those regions of interest (ROI), detecting eyes and smiles.
"""
import cv2

# Load Haar cascade models for tracking face, eyes, and smile contours.
face_cascade = cv2.CascadeClassifier(r"face_and_object_detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"face_and_object_detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"face_and_object_detection\haarcascade_smile.xml")

# Initialize default webcam source
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert frame to grayscale for faster computation and pattern matching
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect all possible faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw a green bounding box around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Create a "Region of Interest" (ROI) explicitly inside the face bounding box.
        # This dramatically increases the performance and accuracy of subsequent eye and smile detections.
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect eyes within the Region of Interest
        # Using a higher scaleFactor/minNeighbors as eyes are smaller details
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            # If so much as 1 eye matches, update the UI label near the top-left of the face
            cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Detect smiles within the same Region of Interest
        # Note the 1.5 scale factor and 15 neighbor threshold to balance false positives and detection
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 15)
        if len(smiles) > 0:
            # Overlap text label near the top-left of the face
            cv2.putText(frame, "Smiling..", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Render final overlay to the user
    cv2.imshow("Smart face detector", frame)
    
    # Graceful exit checking
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destruct components and clean IO devices
cap.release()
cv2.destroyAllWindows()