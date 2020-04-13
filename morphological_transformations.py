import cv2
import numpy as np
import matplotlib.pyplot as plt

#img_path = 'smarties.jpeg'
img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (512, 512))
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# you can try using the mask as input to the filters instead of img
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=2)
erosion = cv2.erode(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # this works good w the parking tickets
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

titles = ['image','mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, img, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
	
plt.show()
