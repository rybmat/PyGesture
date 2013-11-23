import cv2
import numpy as np
import time

class track_hand:
	def __init__(self):
		print "Opening camera..."
		self.camera = cv2.VideoCapture(0)
		cv2.namedWindow("Camera")
		if self.camera.isOpened():
			frame=cv2.imread('hand.jpg',1)
			self.track_window=(100,100,50,50)
			self.hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			self.hsv_roi = self.hsv_roi[:,:,:1]
			self.mask = cv2.inRange(self.hsv_roi, np.array((0)), np.array((10)))
			self.roi_hist = cv2.calcHist([self.hsv_roi],[0],self.mask,[10],[0,10])
		cv2.normalize(self.roi_hist,self.roi_hist,0,255,cv2.NORM_MINMAX)
		self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 1 )
	def track(self):
		working=0
		while True:
			retval, image = self.camera.read()
			if retval:
				flipped = cv2.flip(image,0)
				hsv = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)
        			dst = cv2.calcBackProject([hsv],[0],self.roi_hist,[0,10],1)
        			ret, self.track_window = cv2.CamShift(dst, self.track_window, self.term_crit)
        			x,y,w,h = self.track_window
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
