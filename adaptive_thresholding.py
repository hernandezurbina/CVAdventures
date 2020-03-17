import cv2 as cv

img_path = 'sudoku.jpeg'
img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'
img = cv.imread(img_path, 0)
img = cv.resize(img, (512, 512))


_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('image', img)
cv.imshow('threshold 1', th1)
cv.imshow('threshold 2', th2)
cv.imshow('threshold 3', th3)

cv.waitKey(0)
cv.destroyAllWindows()
