import cv2 as cv
img = cv.imread('a.jpg')
img = cv.line(img, (0,0), (200,200), (255,0,0), 10)
img = cv.arrowedLine(img, (0,0), (150,90), (255,89,0), 7)
img = cv.rectangle(img, (1,2),(90,180),(0,130,90),-1)
img = cv.circle(img,(150,150), 90, (250,250,250), 5)
img = cv.putText(img, 'Hello World!',(100,100), cv.FONT_HERSHEY_SCRIPT_COMPLEX,5,(100,100,1),5)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()