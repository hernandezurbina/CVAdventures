import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
PARKEE NOTE:
does it matter to split the image in 3 channels before processing?
"""


img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

b, g, r = cv2.split(img)

cv2.imshow('original', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
