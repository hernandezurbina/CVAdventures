import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]

for i in range(len(titles)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
