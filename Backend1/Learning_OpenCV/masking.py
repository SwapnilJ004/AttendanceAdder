#Shri Ganeshaya Namaha
import cv2 as cv
import numpy as np

img = cv.imread('./Clear_Attendance.jpg')
cv.imshow('Clear_Attendance', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

rectangle = cv.rectangle(blank, (img.shape[1]//2+100, img.shape[0]//2+100),(img.shape[1]//2+300, img.shape[0]//2+300), 255, -1)
# cv.imshow('Mask', mask)

circle = cv.circle(blank.copy(), (400,400), 400, 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked image', masked)

cv.waitKey(0)