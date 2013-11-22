import cv2
import numpy as np
import time


if __name__ == "__main__":
	print "Opening camera..."
	camera = cv2.VideoCapture(0)
	cv2.namedWindow("Camera")
	if camera.isOpened():
		working=0
		ret,frame=camera.read()
		track_window=(100,100,50,50)
		hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255.)))
		roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
		cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
		term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 1 )
		while True:
			retval, image = camera.read()
			if retval:
				flipped = cv2.flip(image,0)
				hsv = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)
        			dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        			ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        			x,y,w,h = track_window
        			cv2.rectangle(flipped, (x,y), (x+w,y+h), 255,2)
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
