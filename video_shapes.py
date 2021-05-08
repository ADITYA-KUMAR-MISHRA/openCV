import cv2 as cv 
import datetime
cap = cv.VideoCapture(0)
while(True):
    ret , frame = cap.read()
    if ret == True:
        date = str(datetime.datetime.now())
        frame = cv.putText(frame,str(int(cap.get(3)))+'X'+str(int(cap.get(4)))+date,(30,30),cv.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2)
        cv.imshow('Camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q') :
            break
cap.release()