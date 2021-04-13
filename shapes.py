import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)#get area
        print(area)
        if area>50:#select all shapes
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)#draw outer layer of shapes
            peri=cv2.arcLength(cnt,True)#get perimeter
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)#get corner points
            print(len(approx))
            objcor=len(approx)
            x, y, w, h = cv2.boundingRect(approx)#get width,height
            if objcor==3: objectType="Tri"
            elif objcor==4:
                aspectRatio=w/float(h)
                if aspectRatio>0.95 and aspectRatio<1.05: objectType="square"
                else:objectType="Rectangle"
            elif objcor>4: objectType="circle"
            else: objectType="None"

            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)#drawing bounding box
            cv2.putText(imgcontour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,0.5,(0,0,255),2)






img=cv2.imread("cvimages/proj_img1.jpg.")
imgcontour=img.copy()
img_Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_Blur=cv2.GaussianBlur(img_Gray,(7,7),1)
img_canny=cv2.Canny(img_Blur,50,50)
getContours(img_canny)
img_blank=np.zeros_like(img)
img_stack=stackImages(0.8,([img,img_Gray,img_Blur],[img_canny,imgcontour,img_blank]))
cv2.imshow("stack",img_stack)
cv2.waitKey(0)