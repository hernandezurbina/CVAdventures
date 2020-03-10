import numpy as np
import cv2

# list all avail events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		blue = img[y, x, 0]
		green = img[y, x, 1]
		red = img[y, x, 2]
		
		cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
		myColorImage = np.zeros((512, 512, 3), np.uint8)
		myColorImage[:] = [blue, green, red]
		
		cv2.imshow('Color', myColorImage)
		
points = []
img = cv2.imread('image2.jpg', 1)
cv2.imshow('My image', img)

cv2.setMouseCallback('My image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
