import cv2

img = cv2.imread('image2.jpg', 0) # 1 - for loading in color, 0 - grayscale, -1 unchanged
#print(img)
### READ
cv2.imshow('My image', img)
k = cv2.waitKey(0)

if k == 27: # esc key
	cv2.destroyAllWindows()
elif k == ord('s'):
	### WRITE
	cv2.imwrite('image_copy.jpg', img)
	cv2.destroyAllWindows()

