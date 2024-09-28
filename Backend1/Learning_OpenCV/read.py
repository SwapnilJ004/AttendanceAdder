#Shri Ganeshaya Namaha
import cv2 as cv
import numpy as np

img = cv.imread('./Clear_Attendance.jpg')

#Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blurring
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)
# cv.waitKey(0)

#Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)
# cv.waitKey(0)

#Dilating image
# dilated = cv.dilate(canny, (1,1), iterations=1)
# cv.imshow('dilated', dilated)
# cv.waitKey(0)

#Eroding image
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded', eroded)
# cv.waitKey(0)

#Resize
# resized = cv.resize(img, (1000,1000), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
# cv.waitKey(0)

#Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)
# cv.waitKey(0)

#Translation
def translate(img, x, y):
    transMAT = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMAT, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)

#Flipping
#Cropping