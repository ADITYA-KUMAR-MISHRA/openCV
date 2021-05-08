import cv2 as cv 
import  math
import numpy as np 
from random import randint as rd
img = np.zeros([751,751, 3], np.uint8)      #create image of 751 x 751 pixels
cv.circle(img,(376, 376), 375, (255,255,255), 2)  #a circle is drawn from the center
num = int(input('Enter the number of points: '))
cv.imshow('pi',img)
total = 0
for i in range(1,num):
    x = rd(0,750)                   #randomly selects x and y co-ordinates
    y = rd(0,750)
    if(math.sqrt(((376 - x) ** 2) + ((376 - y) ** 2)) <= 375):  #if coordinates lies inside the circle then put green dot on the coordinate
        total += 1
        cv.circle(img,(x,y), 1, (0, 255, 0), -1)
    else:                               #else put red dot on the image at given coordinate
        cv.circle(img,(x,y), 1, (0,0,255), -1)
    c_pi = 4.0 * total/i                #calculate the value of pi
    error = float(abs(math.pi - c_pi)*100/math.pi) #calculate the error
    temp = img.copy()
    cv.putText(temp,"pi = "+str(c_pi)+" % error = "+str(error), (20,20), cv.FONT_HERSHEY_PLAIN, 1.25 , (255, 0 , 0), 2) #put calculated value and percentage error on the image
    cv.imshow('pi', temp)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.waitKey(0)