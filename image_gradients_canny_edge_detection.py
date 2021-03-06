import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelComb']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(len(titles)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
