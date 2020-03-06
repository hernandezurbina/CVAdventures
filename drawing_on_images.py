import cv2
import numpy as np

img = cv2.imread('image2.jpg', 1) # 1 - for loading in color, 0 - grayscale, -1 unchanged
#img = np.zeros([512, 512, 3], np.uint8)

#img = cv2.line(img, (0,0), (255, 255), (0, 255, 0), 10) # color in BGR format

img = cv2.rectangle(img, (384, 200), (520, 400), (0, 255, 0), 10) # top-left point to bottom-right
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Vico', (600, 600), font, 2, (0, 255, 0), 5, cv2.LINE_AA)

cv2.imshow('My image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

