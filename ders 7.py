import cv2 as cv
import numpy as np

img = cv.imread('../advanced lane line/lena.jpg')
cv.namedWindow('lena')

def nothing(x):
    print(x)

cv.createTrackbar('CP', 'lena', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'lena', 0, 1, nothing)

while(True):
    img = cv.imshow('lena', img)
    pos = cv.getTrackbarPos('CP', 'lena')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv.getTrackbarPos(switch, 'lena')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
