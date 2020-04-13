import cv2
import numpy as np

"""
The code here might help to improve
detection in the parquimetros dataset!
Look at the contours in the characters!
"""

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thres = cv2.threshold(imgGray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Num contours: ', str(len(contours)))

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('original', img)
cv2.imshow('gray', imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()