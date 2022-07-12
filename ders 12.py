import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', 0)

lap = cv.Laplacian(img, cv.CV_32FC4, ksize = 3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['img', 'lap', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
