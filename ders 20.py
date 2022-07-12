import numpy as np
import cv2 as cv

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 10, 200, apertureSize= 3)

lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength= 1, maxLineGap= 16)
print(lines)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('image', img)
k = cv.waitKey(0)
cv.destroyAllWindows()
