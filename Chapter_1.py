# Reading an image and displaying it
# import library 
import numpy as np
import cv2 as cv

img = cv.imread("resources/image.jpg")
cv.imshow("Murshid",img)
cv.waitKey(0) 
