import cv2
import numpy as np
import time


if __name__ == "__main__":
	print "Opening camera..."
	camera = cv2.VideoCapture(0)
	working = 0

	cv2.namedWindow("Camera")
	if camera.isOpened():
		while True:
			retval, image = camera.read()
			
			if retval:
				flipped = cv2.flip(image,0)
				cv2.imshow("Camera", flipped)
				if not working:
					print "Camera is working now..."
					working = 1
			
			#break on Escape
			key = cv2.waitKey(20)
			if key == 27:
				break
	else:
		print "Camera is not opened"
