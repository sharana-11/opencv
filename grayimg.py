import cv2
import numpy as np
img=cv2.imread("cvimages/im.jpg")
kernel=np.ones((5,5),np.uint8) #unsigned integer range from 0 to 255
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gray image
imgBlur=cv2.GaussianBlur(img,(7,7),0) #Blur image
imgEdge= cv2.Canny(img, 150,200) #Canny Edge Detector-find edges of an objects in img by Canny Detection Algorithm
imgDilation=cv2.dilate(imgEdge,kernel,iterations=1)# increase thickness that we need
imgErosion=cv2.erode(imgDilation,kernel,iterations=1)# decrease thickness that we need
cv2.imshow("gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgEdge)
cv2.imshow("dialate",imgDilation)
cv2.imshow("Erosion",imgErosion)
cv2.waitKey(0)