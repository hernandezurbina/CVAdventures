import numpy as np
import cv2

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
