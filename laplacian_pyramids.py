import cv2
import numpy as np

"""
The code here might help to improve
detection in the parquimetros dataset!
"""

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

layer = gp[5]
cv2.imshow('Upper level', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
