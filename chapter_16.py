# saving HD recording of cam steaming

import cv2 as cv
import numpy as np


cap= cv.VideoCapture(0)
# resolution HD (1280,720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
def sd_resolution():
    cap.set(3, 680)
    cap.set(4, 480)
def fhd_resolution():
    cap.set(3, 920)
    cap.set(4, 1080)

hd_resolution()
#sd_resolution()
#fhd_resolution()


# writing format, codec, video writer object and file output
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc("M", "j", "P","G"), 30, (frame_width, frame_height))

while(True):
    (ret,frame)= cap.read()
    # to show in player
    if ret == True:
        
        out.write(frame)
        cv.imshow("video", frame)
        # to quit with q key 
        if cv.waitKey(1) & 0xff== ord("q"): 
            break
    else: 
        break
    
cap.release()
out.release()
cv.destroyAllWindows()