# Grayscale converting 
# import library 
import cv2 as cv

img= cv.imread("resources/image.jpg")

# if your picture is too big then you use this line of code
gray_img = cv.resize(img, (800,600))

# conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Pehli image", img)
cv.imshow("Gray image", gray_img)

# Delay code
cv.waitKey(0) 
cv.destroyAllWindows() 



