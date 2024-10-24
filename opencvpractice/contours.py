import cv2 as cv
import numpy as np

img = cv.imread('photos/mc.jpg')
cv.imshow('catto', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_img)

# #GAUSSIAN BLUR
gaussian_blur = cv.GaussianBlur(gray_img, (5,5), cv.BORDER_DEFAULT)

# apply cascade
canny = cv.Canny(gaussian_blur, 125, 125)
cv.imshow('canny', canny)

# ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

# contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} is the number of contours!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours drawn', blank)

cv.waitKey(0) 