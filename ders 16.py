import cv2 as cv
import numpy as np

img = cv.imread('opencv-logo-white.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('number of contours: ' + str(len(contours)))
print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imshow('image', img)
cv.imshow('image gray', imgray)

cv.waitKey(0)
cv.destroyAllWindows()
