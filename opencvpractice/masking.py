import cv2 as cv
import numpy as np

img = cv.imread('photos/catto.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (200, 300), 200, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked', masked)


cv.waitKey(0)