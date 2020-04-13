import cv2
import numpy as np

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'

img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))
lr = cv2.pyrDown(img)

cv2.imshow('Original', img)
cv2.imshow('Pyr down', lr)

cv2.waitKey(0)
cv2.destroyAllWindows()
