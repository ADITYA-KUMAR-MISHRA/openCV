import cv2 as cv 
import datetime
cap = cv.VideoCapture(0)
while(True):
    ret , frame = cap.read()
    dt = str(datetime.datetime.now())
    upd = cv.putText(frame,dt,(50,50), cv.FONT_HERSHEY_PLAIN, 1.5, (7,90,190),2)
    cv.imshow('camera', upd)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
# x = open('hello world.txt', )