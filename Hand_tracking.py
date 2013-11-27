import cv2
import numpy as np
import time


class Track_hand:
	def __init__(self,camera):
		frame=cv2.imread('hand.jpeg', 1)
		self.track_window = (0, 0, 800, 600)
		print self.track_window
		hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		self.kalman1=cv2.cv.CreateKalman(4,2,0)
		self.kalman2=cv2.cv.CreateKalman(4,2,0)
		self.kalman1=self.Kalman_init(self.kalman1,0,0)
		self.kalman2=self.Kalman_init(self.kalman2,800,600)
		
		mask = cv2.inRange(hsv_roi, np.array((0,100.,100.)), np.array((20.,173.,145.)))
		self.roi_hist = cv2.calcHist([hsv_roi], [0], mask, [13], [0, 180])
		
		cv2.normalize(self.roi_hist, self.roi_hist, 0, 255, cv2.NORM_MINMAX)
		self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	def Kalman_init(self,kalman,x,y):
		kalman.transition_matrix[0,0] = 1
		kalman.transition_matrix[1,1] = 1
		kalman.transition_matrix[2,2] = 1
		kalman.transition_matrix[3,3] = 1
		kalman.state_pre[0,0]=x
		kalman.state_pre[1,0]=y
		kalman.state_pre[2,0]=0
		kalman.state_pre[3,0]=0
		cv2.cv.SetIdentity(kalman.measurement_matrix, cv2.cv.RealScalar(1))
		cv2.cv.SetIdentity(kalman.process_noise_cov, cv2.cv.RealScalar(1e-3))## 1e-5
		cv2.cv.SetIdentity(kalman.measurement_noise_cov, cv2.cv.RealScalar(1e-2))
		cv2.cv.SetIdentity(kalman.error_cov_post, cv2.cv.RealScalar(0.1))
		return kalman
	def track(self, image):		
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv], [0], self.roi_hist, [0, 180], 1)
		ret, self.track_window = cv2.CamShift(dst, self.track_window, self.term_crit)
		#print self.track_window
		x, y, w, h = self.track_window
		cv2.cv.KalmanPredict(self.kalman1)
		cv2.cv.KalmanPredict(self.kalman2)
		points1=cv2.cv.CreateMat(2, 1, cv2.cv.CV_32FC1)
		points2=cv2.cv.CreateMat(2, 1, cv2.cv.CV_32FC1)
		points1[0,0]=x; points1[1,0]=y; points2[0,0]=x+w; points2[1,0]=y+h
		estimate1=cv2.cv.KalmanCorrect(self.kalman1,points1)
		estimate2=cv2.cv.KalmanCorrect(self.kalman2,points2)
		x1=int(estimate1[0,0]); x2=int(estimate2[0,0]); y1=int(estimate1[1,0]); y2=int(estimate2[1,0])
		self.track_window=(x1,y1,x2-x1,y2-y1)
		cv2.rectangle(image, (x1,y1),(x2,y2),255, 2)
