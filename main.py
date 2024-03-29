import sys
import numpy as np
import cv2

system = sys.platform
orientation=0

if system == 'darwin':
	print "platform: OSX"
	from OSX_mouse_controller import Mouse
	orientation=1
elif system == 'linux2':
	print "platform: Linux2"
	from Linux_mouse_controller import Mouse
else:
	print "OS not supported, probably Windows ;)"


def scale_mouse_coordinates(m, position, camera):
	(x, y, w, h) = position 
	k1 = m.maxX / camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
	k2 = m.maxY / camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
	return int(k1 * (2 * x + w) / 2), int(k2 * (2 * y + h) / 2)
	
	
if __name__ == '__main__':
	
	palm_cascade = cv2.CascadeClassifier("training_data/training7/palm/cascade.xml")
	fist_cascade = cv2.CascadeClassifier("training_data/training7/fist/cascade.xml")

	print "Opening camera..."
	camera = cv2.VideoCapture(0)
	working = 0
	pos = (500, 500, 100, 100)
	m=Mouse()
	
	cv2.namedWindow("Camera")

	if camera.isOpened():
		while True:
			retval, image = camera.read()

			if retval:
				flipped = cv2.flip(image, orientation)
				img = flipped [:]
				
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				palms = palm_cascade.detectMultiScale(gray, 1.1, 7)
				fists = fist_cascade.detectMultiScale(gray, 1.1, 7)

				for (x, y, w, h) in palms:
					print "palm"
					cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
					pos = (x, y, w, h)

				#movex, movey = scale_mouse_coordinates(m, pos, camera)
				#m.moveTo(movex,movey)

				for (x, y, w, h) in fists:
					print "fist"
					cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
				
				
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
