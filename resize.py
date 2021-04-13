import cv2
import numpy as np
img=cv2.imread("cvimages/mustang.jpg")
print(img.shape)
imgResize=cv2.resize(img,(200,150))
imgcrop=img[0:145,150:300]
cv2.imshow("ironman",img)
cv2.imshow("resized",imgResize)
cv2.imshow("Croped",imgcrop)


cv2.waitKey(0)