import cv2
#import numpy as np
#from time import sleep
#from PIL import Image
#import tkinter as tk
import os


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
            label = None
            confidence = float('inf')
            for name, model in models.items():
                id_, conf = model.predict(roi_gray)
                if conf < confidence:
                    label = name
                    confidence = conf

            # Draw a rectangle around the face and display the predicted label
            if label is not None:
                font = cv2.FONT_HERSHEY_PLAIN
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, label, (x, y - 4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
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