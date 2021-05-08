import cv2 as cv
import numpy as np
img1 = cv.imread('holi.jpg')
img2 = cv.imread('portrait.jpg')
print(img1.shape) # returns a tuple of number of rows, columns, and channels
print(img1.size) # returns total number of pixels
print(img1.dtype) #returns image datatype

b,g,r = cv.split(img1)
# print(img1)
ex = np.zeros(list(img1.shape), np.uint8)

cv.imshow('blue',b)
cv.imshow('green', g)
cv.imshow('red', r)
cv.waitKey(0)
cv.destroyAllWindows()