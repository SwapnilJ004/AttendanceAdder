#Shri Ganeshaya Namaha
import cv2 as cv

img = cv.imread('./Clear_Attendance.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)


# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contour(s) found:')
cv.waitKey(0)