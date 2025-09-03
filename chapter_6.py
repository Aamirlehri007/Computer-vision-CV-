# reading a video 

import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

# Indicator added
if (cap.isOpened() == False):
    print("error in uploading video")
    
# reading and playing 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("video", frame)
        if cv.waitKey(1) & 0xff== ord("q"): 
            break
    else: 
        break
cap.release()
cv.destroyAllWindows() 