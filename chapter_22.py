# face detection ein images
import cv2 as cv


face_cascade = cv.CascadeClassifier("resources/haarcascade_eye.xml") 
img = cv.imread("resources/aamir.jpg")
gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img, 1.1,4)

# draw a rectangle 

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

#img = cv.resize(img,(400,400))
#print(img.shape)
cv.imshow("image",img)
# i want to save this image the use below code
cv.imwrite("resources/face.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()
