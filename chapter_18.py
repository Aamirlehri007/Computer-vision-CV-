# how to change the perspective of an image

import cv2 as cv
import numpy as np

img= cv.imread("resources/download.png")
print(img.shape)
# defining points
point1 = np.float32([[73,62],[156,42],[60,170],[185,200]])
width = 211
height = 239

point2= np.float32([[0,0],[211,0],[0,239],[211,239]])
matrix = cv.getPerspectiveTransform(point1,point2)
out_img= cv.warpPerspective(img, matrix, (width ,height))

cv.imshow("Origional", img)
cv.imshow("transformed", out_img)
#cv.imwrite("resources/warp_perpective.png",out_img)
cv.waitKey(0)
cv.destroyAllWindows()
