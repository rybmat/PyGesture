import sys
import cv2
from time import sleep
from Hand_tracking import Track_hand

system = sys.platform
if system == 'darwin':
	print "platform: OSX"
	from OSX_mouse_controller import Mouse
elif system == 'linux2':
	print "platform: Linux2"
	from Linux_mouse_controller import Mouse
else:
	print "OS not supported, probably Windows ;)"



if __name__ == '__main__':
	
	print "Opening camera..."
        camera = cv2.VideoCapture(0)
        working = 0

        STEP = 10
        m = Mouse()
        a = Track_hand()

        cv2.namedWindow("Camera")
        if camera.isOpened():
                while True:
                        retval, image = camera.read()
                        
                        if retval:
                                flipped = cv2.flip(image,1)
                                a.track(flipped)
                                x, y, w, h = a.track_window
                                m.moveTo((2 * x + w) / 2, (2 * y + h) / 2)
                                
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


