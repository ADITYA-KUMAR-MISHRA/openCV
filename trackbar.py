import cv2 as cv 
import numpy as np 
def nothing(x):
    pass 
img = np.zeros([500, 500, 3], np.uint8)
cv.namedWindow('img')
cv.createTrackbar('R', 'img', 0, 255 , nothing)
cv.createTrackbar('G', 'img', 0 , 255 , nothing)
cv.createTrackbar('B', 'img', 0, 255 , nothing)
cv.createTrackbar('on/off', 'img', 0,1, nothing)
while(1):
    if(cv.getTrackbarPos('on/off', 'img')):
        r = cv.getTrackbarPos('R', 'img')
        g = cv.getTrackbarPos('G', 'img')
        b = cv.getTrackbarPos('B', 'img')
        img[:] = [b,g,r]
    else :
        img[:] = [0, 0, 0]
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break