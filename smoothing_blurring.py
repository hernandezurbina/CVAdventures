import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'Parquimetros/2018-12-22 17.27.43.jpg'

img = cv2.imread(img_path)
img = cv2.resize(img, (512, 512))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel) # smoothes corners
blur = cv2.blur(img, (5, 5))
g_blur = cv2.GaussianBlur(img, (5, 5), 0) # reduces high freq noise
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Orig', '2D Conv', 'Blur', 'GBlur', 'Median', 'Bilateral']
images = [img, dst, blur, g_blur, median, bilateralFilter]

for i in range(len(titles)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
