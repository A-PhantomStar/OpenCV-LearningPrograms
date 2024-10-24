import cv2 as cv
import numpy as np

img = cv.imread('photos/mc.jpg')
cv.imshow('mc', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('bluegray', b)
cv.imshow('greengray', g)
cv.imshow('redgray', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# show in no gray scale
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)