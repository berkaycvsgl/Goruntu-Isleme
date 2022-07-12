import cv2 as cv

img = cv.imread('../advanced lane line/lena.jpg')
lower = img.copy()

gaussian_pyr = [lower]
for i in range(3):
    lower = cv.pyrDown(lower)
    gaussian_pyr.append(lower)

laplacian_top = gaussian_pyr[-1]

laplacian_pyr = [laplacian_top]
for i in range(3, 0, -1):
    gaussian_expanded = cv.pyrUp(gaussian_pyr[i])
    laplacian  = cv.subtract(gaussian_pyr[i-1], gaussian_expanded)
    laplacian_pyr.append(laplacian)
    cv.imshow('lap-{}'.format(i-1), laplacian)
    cv.waitKey(0)
