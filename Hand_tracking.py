import cv2
import numpy as np
import time


class Track_hand:
	iterations=0
	def __init__(self,camera):
		self.hand_square_history=[]
		self.kalman1=cv2.cv.CreateKalman(4,2,0)
		self.kalman2=cv2.cv.CreateKalman(4,2,0)
		self.kalman1=self.Kalman_init(self.kalman1,0,0)
		self.kalman2=self.Kalman_init(self.kalman2,800,600)
		self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
		self.track_window=(0,0,800,600)
	
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
	
	def cutTrackedImg(self,img):
		x,y,w,h=self.track_window
		cut=img[y:y+h,x:x+w]
		tmp=cv2.cvtColor(cut,cv2.COLOR_BGR2HSV)
		tmp=cv2.inRange(tmp,np.array((0,0,0)),np.array((13,255,255)))
		t=cv2.findContours(tmp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_KCOS)
		for el in t[0]:
			moments=cv2.moments(el)
			for i in el:
				i[0,0]=i[0,0]+x
				i[0,1]=i[0,1]+y
			if moments['m00']>100:
				self.hand_square_history.append(moments['m00'])
				cv2.drawContours(img,[el],-1,(0,255,0),3)
		return img
		

	def track(self, image,hmin,hmax,smin,smax,vmin,vmax):
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, np.array((hmin,smin,vmin)), np.array((hmax,smax,vmax)))
		roi_hist = cv2.calcHist([hsv], [0], mask, [180], [0, 180])
		cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
		dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
		if self.__class__.iterations>30:
			ret, self.track_window = cv2.CamShift(dst, self.track_window, self.term_crit)
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
		else:
			self.__class__.iterations+=1
		return dst
