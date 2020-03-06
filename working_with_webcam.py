import cv2

cap = cv2.VideoCapture(0) # filename 'file.avi' or device index e.g. 0 or -1

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
out = cv2.VideoWriter('output.avi', fourcc, fps, (640, 480)) # fourcc code: video codec

#while True:
while cap.isOpened():
	ret, frame = cap.read() # ret True if frame is available
	if ret:
		### change frame props
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		#print(cap.get(cv2.CAP_PROP_FPS)) # 30fps
		
		## save to file
		out.write(frame)
		
		#cv2.imshow('My camera', gray)
		cv2.imshow('My camera', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
