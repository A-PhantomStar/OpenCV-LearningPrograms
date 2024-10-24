import cv2 as cv

img = cv.imread('photos/mc.jpg')
cv.imshow('mc', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('av', average)

# gaussian blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian', gaussian)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)