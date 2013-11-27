import cv2
import numpy as np
import time


if __name__ == "__main__":
	print "Opening camera..."
	camera = cv2.VideoCapture(0)
	working = 0
	i = 0
	cv2.namedWindow("Camera")
	if camera.isOpened():
		with open("training_data/bg.txt", "w") as f:
			while True:
				retval, image = camera.read()
				
				if retval:
					flipped = cv2.flip(image, 1)
					cv2.imshow("Camera", flipped)
					name = "bg_img/image" + str(i) + ".jpg"
					i += 1
					r = cv2.imwrite("training_data/" + name, flipped)
					f.write(name + "\n")
					print r
					if not working:
						print "Camera is working now..."
						working = 1
				
				#break on Escape
				key = cv2.waitKey(20)
				if key == 27:
					break
	else:
		print "Camera is not opened"