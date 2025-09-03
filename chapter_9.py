# how to capture a webcam inside python 

# step-1 import libraries
import cv2 as cv
import numpy as np

# step-2 read the frame from camera
 
cap = cv.VideoCapture(0) # webcam no 1

#  read untill the end
# step-3 Display frame by frame 


while(cap.isOpened()):
    # capture frame by frame
    ret,frame = cap.read()
    if ret== True:
        # to display the frame
        cv.imshow("Frame", frame)
        # to quit with q key 
        if cv.waitKey(1) & 0xff== ord("q"): 
            break
    else:
        break
        
# release or close the windows easily 
cap.release()
cv.destroyAllWindows()