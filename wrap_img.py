import cv2
import numpy as np
img=cv2.imread("cvimages/cards.jpg")
width,height=350,500
pts1=np.float32([[166,229],[323,229],[322,445],[167,445]])
pts2=np.float32([[0,0],[width,0],[height,width],[0,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Mustang",img)
cv2.imshow("King",imgOutput)
cv2.waitKey(0)