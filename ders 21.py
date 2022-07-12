from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

image = cv.imread('road1.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2 , height/2),
    (width, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(image, np.array([region_of_interest_vertices], np.int32))


plt.imshow(cropped_image)
plt.show()
