import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

img1 = cv.imread('photos/catto.jpg')
# cv.imshow('canvas', blank)

#paint image certain color
blank[200:300, 300:400] = 255,200,1
# cv.imshow('canvas1', blank)

#draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,250), thickness=cv.FILLED)
# cv.imshow('canvas1', blank)

#draw circle
cv.circle(blank, (300,300), 40, (255,0,0), thickness=2)
# cv.imshow('canvas3', blank)

#draw line
cv.line(blank, (0, 0), (500, 500), (255,255,255), thickness=5)
# cv.imshow('canvas4', blank)

#write text
cv.putText(blank, 'Hello world! Using OpenCV', (0,450), cv.FONT_HERSHEY_COMPLEX, 0.75, (255,0,255), 1)
cv.imshow('canvasTEXT', blank)


cv.waitKey(0)