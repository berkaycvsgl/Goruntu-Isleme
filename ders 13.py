import cv2 as cv

img = cv.imread('../advanced lane line/lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #imshow(str(i), layer)

layer = gp[5]
cv.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)


cv.imshow('original image', img)
cv.waitKey(0)
cv.destroyAllWindows()
