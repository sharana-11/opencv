import cv2
import numpy as np
img=cv2.imread("cvimages/mustang.jpg")
hor_img=np.hstack((img,img))
cv2.imshow("horizontal",hor_img)
ver_img=np.vstack((img,img))
cv2.imshow("vertical",ver_img)
hor_1=cv2.hconcat(img,img)
cv2.imshow("HORIZONTAL",img)
cv2.waitKey(0)