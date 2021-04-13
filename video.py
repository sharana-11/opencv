import cv2
cap= cv2.VideoCapture("cvimages/swara.mp4")
while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(2) & 0xFF==ord('q'):
        break
