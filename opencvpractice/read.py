import cv2 as cv

def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




# img1 = cv.imread('photos/catto.jpg')
# img2 = cv.imread('photos/catto2.jpg')

# resized_img1 = rescaleFrame(img1)
# resized_img2 = rescaleFrame(img2)


# cv.imshow('cat', resized_img1)
# cv.imshow('cato', resized_img2)


# cv.waitKey(0)


capture = cv.VideoCapture('video/fuuka1080p.mp4')

while True:
    isTrue, frame = capture.read()
    vid_resized = rescaleFrame(frame, .25)

    cv.imshow('Video', vid_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

