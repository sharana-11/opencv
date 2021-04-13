import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
# print(img)
# cv2.imshow("image",img)
cv2.line(img,(0,0),(300,300),(0,0,255),3)# to get line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(100,250,255),3)#to get diagonal
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)#to get rectangle
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)#to get triangle filled with color
cv2.circle(img,(400,50),30,(255,0,255),5)#to get circle
cv2.putText(img,"PYTHON",(300,250),cv2.FONT_ITALIC,1,(150,100,150),5)# insert a text on image


cv2.imshow("line",img)
cv2.waitKey(0)