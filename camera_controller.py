import cv2
import numpy as np
import time

class track_hand:
	def __init__(self):
		print "Opening camera..."
		self.camera = cv2.VideoCapture(0)
		self.frame_width=self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
		self.frame_height=self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
		cv2.namedWindow("Camera")
		self.last_track_window=[0,0,0,0]
		if self.camera.isOpened():
			frame=cv2.imread('hand.jpg',1)
			self.track_window=(100,100,50,50)
			hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			kernel=np.ones((5,5),np.float32)/25
			hsv_roi=cv2.dilate(hsv_roi, kernel,iterations=2)
			hsv_roi=cv2.erode(hsv_roi, kernel,iterations=2)
			hsv_roi = hsv_roi[:,:,:2]
			mask = cv2.inRange(hsv_roi, np.array((5,59)), np.array((9,170)))
			self.roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
			cv2.normalize(self.roi_hist,self.roi_hist,0,255,cv2.NORM_MINMAX)
			self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
	def track(self):
		#while True:
			self.last_track_window=self.track_window
			retval, image = self.camera.read()
			if retval:
				flipped = cv2.flip(image,0)
				hsv = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)
        			dst = cv2.calcBackProject([hsv],[0],self.roi_hist,[0,180],1)
        			ret, self.track_window = cv2.CamShift(dst, self.track_window, self.term_crit)
        			x,y,w,h = self.track_window
        			cv2.rectangle(flipped, (x,y), (x+w,y+h), 255,2)
				cv2.imshow("Camera", flipped)
				key=cv2.waitKey(5)
				return key
			#break on Escape
			else:
				print "Camera is not opened"
