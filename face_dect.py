import cv2
# import numpy as np
face_cascade=cv2.CascadeClassifier("cvimages/haarcascade_frontalface_default.xml")#cascade
img=cv2.imread("cvimages/group-of-friends.jpg")
faces=face_cascade.detectMultiScale(img,1.1,4)
for (x,y,w,h) in faces:#creating bounding boxes
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)#diagonal points((x + w, y + h)
cv2.imshow("Face",img)
cv2.waitKey(0)