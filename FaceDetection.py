import numpy as np
import cv2
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello = ('192.168.10.1', 8889)
sock.bind(('',9000))

face_cascade = cv2.CascadeClassifier('Res/haarcascade_frontalface_default.xml')
command = 'command'
streamon = 'streamon'
cmmd = command.encode()
stron = streamon.encode()
sent = sock.sendto(cmmd, tello)
sent = sock.sendto(stron, tello)

cap = cv2.VideoCapture('udp://@0.0.0.0:11111')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]



    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
