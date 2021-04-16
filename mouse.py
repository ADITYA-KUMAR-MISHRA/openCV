import cv2 as cv
import numpy as np 
from random import randint as rd
# prev = []
# def setcallback(event , x , y , flags , param ):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.putText(img, str(x)+" "+str(y), (x,y), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255) , 2)
#         cv.imshow('image', img)
# img = np.zeros([750, 750, 3], np.uint8)
# cv.imshow('image', img)
# cv.setMouseCallback('image', setcallback)
# cv.waitKey(0)
# cv.destroyAllWindows()
def click_event(event, x , y , flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        if len(prev) == 0:
            cv.circle(img, (x,y) , 1 , (rd(0,255), rd(0,255) , rd(0,255)) , -1)
            cv.imshow('image', img)
            prev.append(x)
            prev.append(y)
        else:
            cv.line(img,(prev[0], prev[1]), (x,y), (rd(0,255),rd(0,255),rd(0,255)), 1)
            cv.imshow('image', img)
            prev[0] = x 
            prev[1] = y
img = np.zeros([750, 750, 3], np.uint8)
cv.imshow('image', img)
prev = []
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()