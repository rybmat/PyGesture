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


def scale_coordinates(m,cam):
	x2,y2,w2,h2=a.track_window
	k1=m.maxX/cam.frame_width
	k2=m.maxY/cam.frame_height
	return int(k1*(2*x2+w2)/2), int(k2*(2*y2+h2)/2)

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
                                movex,movey=scale_coordinates(m,a)
                                m.moveTo(movex,movey)
                                
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

    	cv2.destroyAllWindows()
		

