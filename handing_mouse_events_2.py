import numpy as np
import cv2

# list all avail events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
		points.append((x, y))
		
		if len(points) >= 2:
			cv2.line(img, points[-1], points[-2], (0, 255, 0), 5)
		
		cv2.imshow('My image', img)
		
points = []
img = cv2.imread('image2.jpg', 1)
cv2.imshow('My image', img)

cv2.setMouseCallback('My image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
