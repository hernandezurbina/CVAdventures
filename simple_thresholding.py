import cv2 as cv

img = cv.imread('image2.jpg')

# THRES_BINARY
# if the value of the pixel < 127, the value is assigned to 0
# if the value is > 127 the value is assigned 255
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# THRES_BINARY_INV
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

# THRES_TRUNC
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# THRES_TOZERO
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# THRES_TOZERO_INV
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow('image', img)
#cv.imshow('threshold 1', th1)
#cv.imshow('threshold 2', th2)
#cv.imshow('threshold 3', th3)
#cv.imshow('threshold 4', th4)
cv.imshow('threshold 5', th5)

cv.waitKey(0)
cv.destroyAllWindows()
