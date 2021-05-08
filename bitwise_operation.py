import cv2 as cv 
import numpy as np 
img1  = np.zeros([750, 750, 3], np.uint8);
img2  = img1.copy()
img1 = cv.rectangle(img1, (250,250), (500, 500), (255, 255, 255), -1)
img2 = cv.rectangle(img2, (0, 350), (750, 750), (255, 255, 255), -1)
cv.imshow('img1', img1)
cv.imshow('img2', img2)
bitwise_and = cv.bitwise_and(img1, img2)
bitwise_or = cv.bitwise_or(img1, img2)
bitwise_xor = cv.bitwise_xor(img1, img2)
bitwise_not = cv.bitwise_not(img1)
cv.imshow('bitwise and', bitwise_and)
cv.imshow('bitwise or', bitwise_or)
cv.imshow('bitwise xor', bitwise_xor)
cv.imshow('bitwise not', bitwise_not)
cv.waitKey(0)
cv.destroyAllWindows()