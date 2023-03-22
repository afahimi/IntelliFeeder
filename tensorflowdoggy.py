import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained model from the H5 file
model = load_model('dogcat.h5')

# Define the class labels for the model
class_labels = ['cat', 'dog']

# Initialize the camera capture
cap = cv2.VideoCapture(0)

# Loop over the video frames
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Preprocess the frame for the model
    frame = cv2.resize(frame, (224, 224))
    frame = frame.astype('float') / 255.0
    frame = np.expand_dims(frame, axis=0)

    # Use the model to classify the frame
    predictions = model.predict(frame)
    class_idx = np.argmax(predictions[0])
    label = class_labels[class_idx]

    # Display the classification label on the frame
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera capture and close all windows
cap.release()
cv2.destroyAllWindows()
