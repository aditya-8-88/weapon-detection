import cv2
import os

# Step 1: Data Storage
face_data_path = 'face_data'

# Create the face data directory if it doesn't exist
if not os.path.exists(face_data_path):
    os.makedirs(face_data_path)

# Step 2: Face Detection
# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Live Face Detection
video_capture = cv2.VideoCapture(0)  # 0 represents the default camera index
face_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces and save them as images
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save the face image
        face_image = frame[y:y + h, x:x + w]
        face_filename = os.path.join(face_data_path, f'face_{face_count}.jpg')
        cv2.imwrite(face_filename, face_image)

        # Increment the face count
        face_count += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop if 'q' is pressed or a certain number of faces are saved
    if cv2.waitKey(1) & 0xFF == ord('q') or face_count >= 10:
        break

# Release the video capture and destroy any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
