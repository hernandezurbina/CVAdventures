import numpy as np
import cv2

# list all avail events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		text = str(x) + ',' + str(y)
		cv2.putText(img, text, (x, y), font, 0.5, (0, 255, 0), 2)
		cv2.imshow('My image', img)
	if event == cv2.EVENT_RBUTTONDOWN:
		blue = img[y, x, 0]
		red = img[y, x, 1]
		green = img[y, x, 2]
		font = cv2.FONT_HERSHEY_SIMPLEX
		text = str(blue) + ',' + str(green) + ',' + str(red)
		cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 255), 2)
		cv2.imshow('My image', img)
		
		
img = cv2.imread('image2.jpg', 1)
cv2.imshow('My image', img)

cv2.setMouseCallback('My image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
