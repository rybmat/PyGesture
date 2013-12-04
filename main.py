import sys
import cv2
from time import sleep
from Hand_tracking import Track_hand


orientation=0
system = sys.platform
if system == 'darwin':
	print "platform: OSX"
	orientation=1
	from OSX_mouse_controller import Mouse
elif system == 'linux2':
	print "platform: Linux2"
	from Linux_mouse_controller import Mouse
else:
	print "OS not supported, probably Windows ;)"

hmin=0
hmax=14
smin=61
smax=192
vmin=168
vmax=234

def button_down_effect(m,history):
	while len(history)>200:
		del history[0]
	if not history:
		return
	maxsq=max(history)
	minsq=min(history)
	k=(maxsq+minsq)/2
	if history[len(history)-1]<100:
		m.leftButtonDown()
	else:
		m.leftButtonUp()

def trackf(a):
	pass

def scale_coordinates(m, cam, frameWidth, frameHeight):
	x2, y2, w2, h2 = a.track_window
	k1 = m.maxX / frameWidth
	k2 = 0.5*m.maxY / frameHeight

	return int(k1 * (2 * x2 + w2) / 2), int(k2 * (2 * y2 + h2) / 2)

if __name__ == '__main__':
	cv2.namedWindow("HSV values")
	cv2.cv.CreateTrackbar("hmin","HSV values",hmin,255,trackf)
	cv2.cv.CreateTrackbar("hmax","HSV values",hmax,255,trackf)
	cv2.cv.CreateTrackbar("smin","HSV values",smin,255,trackf)
	cv2.cv.CreateTrackbar("smax","HSV values",smax,255,trackf)
	cv2.cv.CreateTrackbar("vmin","HSV values",vmin,255,trackf)
	cv2.cv.CreateTrackbar("vmax","HSV values",vmax,255,trackf)
	print "Opening camera..."
        camera = cv2.VideoCapture(0)
        working = 0

        STEP = 10
        m = Mouse()
        a = Track_hand(camera)

	cv2.namedWindow("Projection")
        cv2.namedWindow("Camera")
        if camera.isOpened():
                while True:
                        retval, image = camera.read()
                        
                        if retval:
				hmin=cv2.getTrackbarPos("hmin","HSV values")
				hmax=cv2.getTrackbarPos("hmax","HSV values")
				smin=cv2.getTrackbarPos("smin","HSV values")
				smax=cv2.getTrackbarPos("smax","HSV values")
				vmin=cv2.getTrackbarPos("vmin","HSV values")
				vmax=cv2.getTrackbarPos("vmax","HSV values")
                                flipped = cv2.flip(image,orientation)
                                tmp=a.track(flipped,hmin,hmax,smin,smax,vmin,vmax)
                                flipped = a.cutTrackedImg(flipped)
                                movex, movey = scale_coordinates(m, a, camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH), camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
                                m.moveTo(movex, movey)
                               	button_down_effect(m,a.hand_square_history) 
                                cv2.imshow("Camera", flipped)
				cv2.imshow("Projection",tmp)
                                if not working:
                                        print "Camera is working now..."
                                        working = 1
                        
                        #break on Escape
                        key = cv2.waitKey(20)
                        if key == 27:
                                break
        else:
                print "Camera is not opened"

    	cv2.destroyAllWindows()
