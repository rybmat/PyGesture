import sys
import numpy as np
import cv2

system = sys.platform
if system == 'darwin':
	print "platform: OSX"
	from OSX_mouse_controller import Mouse
elif system == 'linux2':
	print "platform: Linux2"
	from Linux_mouse_controller import Mouse
else:
	print "OS not supported, probably Windows ;)"


	
if __name__ == '__main__':
	hand_cascade = cv2.CascadeClassifier("training_data/training6/palm/cascade.xml")

	print "Opening camera..."
	camera = cv2.VideoCapture(0)
	working = 0

	cv2.namedWindow("Camera")
	if camera.isOpened():
		while True:
			retval, image = camera.read()
			
			if retval:
				flipped = cv2.flip(image, 1)
				img = flipped [:]
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				hands = hand_cascade.detectMultiScale(gray, 1.7, 6)
				print "hands"
				for (x, y, w, h) in hands:
					
					cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
					roi_gray = gray[y:y+h, x:x+w]
					roi_color = img[y:y+h, x:x+w]



				cv2.imshow("Camera", img)
				if not working:
					print "Camera is working now..."
					working = 1
			
			#break on Escape
			key = cv2.waitKey(20)
			if key == 27:
				break
	else:
		print "Camera is not opened"
