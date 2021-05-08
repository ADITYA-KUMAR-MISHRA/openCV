import cv2 as cv 
# # function to read image
img = cv.imread('a.jpg')
# # function to show image with arguements as image and name of the window
# cv.imshow('image name', img)
# # function to wait for key to be pressed in millisecond 0 for infinite time 
# cv.waitKey(1000) & 0xFF == ord('q')


# To capture video

# function with arguement as name of the video or 0/-1/2... for default camera 
# cap = cv.VideoCapture(0)
# while(True):
#     ret , frame = cap.read()
#     cv.imshow('frame',frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cap.destroyAllWindows()

# function to convert the image into other color space
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
# if cv.waitKey(0) & 0xFF == ord('q'):
#     cv.destroyAllWindows()

#function to write video
# vid = cv.VideoCapture(0)
# frame_width = int(vid.get(3))
# frame_height = int(vid.get(4))
# size = (frame_width, frame_height)
# result = cv.VideoWriter('filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, size)
# while(True):
#     ret , frame = vid.read()
#     cv.imshow('Color', frame)
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('Gray', gray)
#     result.write(gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# result.release()
# cv.destroyAllWindows()
