import cv2

cap = cv2.VideoCapture(0) # filename 'file.avi' or device index e.g. 0 or -1

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
out = cv2.VideoWriter('output.avi', fourcc, fps, (640, 480)) # fourcc code: video codec

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # id: 3
#cap.set(4, 720) # 4: height

#while True:
while cap.isOpened():
	ret, frame = cap.read() # ret True if frame is available
	if ret:
		### change frame props
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		#print(cap.get(cv2.CAP_PROP_FPS)) # 30fps
		
		## save to file
		out.write(frame)
		
		## write to frame
		font = cv2.FONT_HERSHEY_SIMPLEX
		text = str(cap.get(3)) + "x" + str(cap.get(4)) + \
		" FPS: " + str(cap.get(cv2.CAP_PROP_FPS))
		frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
		
		#cv2.imshow('My camera', gray)
		cv2.imshow('My camera', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
