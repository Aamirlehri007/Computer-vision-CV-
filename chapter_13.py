# basic functions or manupulation in open CV

import cv2 as cv
import numpy as np 
img= cv.imread("resources/aamir.jpg")

# resize
#resize_img= cv.resize(img,(450,150))

# gray
#gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurred image
#blurr_img= cv.GaussianBlur(img, (7,7), 0)

# edge detection 
edge_img= cv.Canny(img, 53,53)

# thickness of line
mat_kernel = np.ones((3,3), np.uint8)
dilated_img= cv.dilate(edge_img, (mat_kernel), iterations=1)

# make thinner outline 
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)


# cropping (we will use numpy library not open CV)
print("the size of our image is:", img.shape)
cropped_img = img[0:500, 0:400]

cv.imshow("Original", img)
#cv.imshow("Resize", resize_img)
#cv.imshow("gray", gray_img)
#cv.imshow("Blurred", blurr_img)
#cv.imshow("Edged", edge_img)
#cv.imshow("Dilated", dilated_img)
#cv.imshow("Erosion", ero_img)
cv.imshow("Cropped", cropped_img) 


cv.waitKey(0) 
cv.destroyAllWindows()