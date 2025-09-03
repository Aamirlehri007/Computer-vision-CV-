# Resizing
# import library 
import numpy as np
import cv2 as cv

img= cv.imread("resources/image.jpg")

# if your picture is too big then you use this line of code
#mg1= cv.resize(img, 800,600) 

cv.imshow("Murshid",img)
#v.imshow("Dosri Image",img1)
cv.waitKey(0) 
cv.destroyAllWindows() 


