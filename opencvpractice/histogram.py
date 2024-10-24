import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/mc.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('circle', mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0],  None, [256], [0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)