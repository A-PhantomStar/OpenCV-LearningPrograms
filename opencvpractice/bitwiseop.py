import cv2 as cv
import numpy as np

blank = np.zeros((200,200), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (15,15), (185,185), 255, -1)
circle = cv.circle(blank.copy(), (100,100), 100, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# BITWISE AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# BITWISE OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

# bitwise xor --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)



cv.waitKey(0)