# writing videos form cam 

import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

# writing format, codec, video writer object and file output

frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc("M", "j", "P","G"), 30, (frame_width, frame_height))


while(True):
    (ret,frame)= cap.read()
    grayframe= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # to show in player
    if ret == True:
        
        out.write(grayframe)
        cv.imshow("video", grayframe)
        # to quit with q key 
        if cv.waitKey(1) & 0xff== ord("q"): 
            break
    else: 
        break
    
cap.release()
out.release()
cv.destroyAllWindows() 