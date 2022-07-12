import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((3, 3), np.uint8)

dilation = cv.dilate(mask, kernal, iterations = 1)
erosion = cv.erode(mask, kernal, iterations = 3)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)

titles = ['smarties', 'mask', 'dilation', 'erosion', 'opening',
          'closing', 'mg']
images = [img, mask, dilation, erosion, opening, closing, mg]

for i in range(7):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


cv.waitKey(0)
