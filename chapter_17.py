# Joining two Images

import cv2 as cv
import numpy as np

img = cv.imread("resources/aamir.jpg")

# stacking same image
# 1- Horizontal stack 

hor_img = np.stack((img,img))
hor_img = np.hstack((img, img))


# 2- Veritical stack
ver_img= np.vstack((img,img))

cv.imshow("Horizontal", hor_img)
cv.imshow("vertical", ver_img)
cv.waitKey(0)
cv.destroyAllWindows() 

# you can only stack images with same shape(with, height, channel)
# your can not resize the stack images (But using different fucntion)
# same number of channels np function 

(600, 500, 3)
# you have to define a function to stack multiple images of different sizes and tunes

