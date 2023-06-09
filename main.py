import cv2
import numpy as np
import tkinter as tk
import os
import subprocess
import requests

def main_app():
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained models for each person
    models = {}
    for filename in os.listdir('./data/classifiers'):
        if filename.endswith('.xml'):
            name = filename.split('_')[0]
            model = cv2.face.LBPHFaceRecognizer_create()
            model.read(f'./data/classifiers/{filename}')
            models[name] = model

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]

            # Use each model to predict the person in the current face
            recognized_users = []
            confidence = 100  # Initialize confidence to a high value
            for name, model in models.items():
                id_, conf = model.predict(roi_gray)
                if conf < confidence:
                    recognized_users.append(name)
                    confidence = conf

            # Draw a rectangle around the face and display the predicted label
            if recognized_users:
                font = cv2.FONT_HERSHEY_PLAIN
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, recognized_users[0], (x, y - 4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

                # If a recognized user exists, launch the desired program
                # Get the current working directory
                cwd = os.getcwd()

                # Navigate to the directory that contains the file
                path_to_file = os.path.join(cwd, 'list_of_accessory.py')

                # Check if the file exists
                if os.path.exists(path_to_file):
                    # If the file exists, launch it with subprocess
                    subprocess.Popen(['python', path_to_file])
                else:
                    print(f"The file {path_to_file} does not exist.")
            else:
                font = cv2.FONT_HERSHEY_PLAIN
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                frame = cv2.putText(frame, "Unknown Person", (x, y - 4), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main_app()