import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("gradient.png", 0)

ret, thresh1 = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 20, 255, cv.THRESH_TRUNC)
ret, thresh3 = cv.threshold(img, 2, 255, cv.THRESH_TOZERO)
ret, thresh4 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)

titles = ['binary', 'trunc', 'tozero', 'binary_inv']
images = [thresh1, thresh2, thresh3, thresh4]

for i in range(4):
    plt.subplot(3, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.imshow("original", img)
cv.imshow("binary", thresh1)
cv.imshow("trunc", thresh2)
cv.imshow("tozero", thresh3)
cv.imshow("binaryinv", thresh4)

 while True:
     key = cv.waitKey(10) & 0xFF
     if key == 27:
         break

cv.destroyAllWindows()
