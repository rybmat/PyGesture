import cv2
import numpy as np
import time

class Track_hand:
	
	def __init__(self):

		frame=cv2.imread('hand.jpeg', 1)
		self.track_window = (0, 0, 640, 480)
		print self.track_window

		hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		kernel = np.ones((5, 5), np.float32) / 25
		hsv_roi = cv2.dilate(hsv_roi, kernel, iterations=2)
		hsv_roi = cv2.erode(hsv_roi, kernel, iterations=2)
		#print(hsv_roi)
		
		hsv_roi = hsv_roi[:,:,:2]
		mask = cv2.inRange(hsv_roi, np.array((5, 59)), np.array((10, 170)))
		self.roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
		
		cv2.normalize(self.roi_hist, self.roi_hist, 0, 255, cv2.NORM_MINMAX)
		self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
	

	def track(self, image):		
				
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv], [0], self.roi_hist, [0, 180], 1)
		
		ret, self.track_window = cv2.CamShift(dst, self.track_window, self.term_crit)
		#print self.track_window
		x, y, w, h = self.track_window

		cv2.rectangle(image, (x, y), (x + w, y + h), 255, 2)
