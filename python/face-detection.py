
# Author: https://github.com/douglascarlini

# pip install face-recognition
# pip install opencv-python

import face_recognition as fr
import cv2

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    rgb = frame[:, :, ::-1]

    faces = fr.face_locations(rgb)

    for y1, x2, y2, x1 in faces:

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
