import cv2
import face_recognition

# Load the known faces and their names
known_faces = []
known_names = []

# Load the images and encode the faces
image1 = face_recognition.load_image_file("photos/justin1.jpg")
face_encoding1 = face_recognition.face_encodings(image1)[0]
known_faces.append(face_encoding1)
known_names.append("Justin")

image2 = face_recognition.load_image_file("photos/justin2.jpg")
face_encoding2 = face_recognition.face_encodings(image2)[0]
known_faces.append(face_encoding2)
known_names.append("Justin")

image3 = face_recognition.load_image_file("photos/justin3.jpg")
face_encoding3 = face_recognition.face_encodings(image3)[0]
known_faces.append(face_encoding3)
known_names.append("Justin")

# Connect to the camera
cap = cv2.VideoCapture(0)

# Capture and display the video stream
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # START SHOWING THE FACE FRAME
    # Convert the frame from BGR to RGB
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and their encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face to the known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # Find the best match
        match_index = matches.index(True) if True in matches else -1
        name = known_names[match_index] if match_index >= 0 else "Unknown"

        # Draw a box around the face and label it
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # END
    
    cv2.imshow('Internal Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()