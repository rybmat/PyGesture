import sys
from time import sleep

system = sys.platform
if system == 'darwin':
	print "platform: OSX"
	from OSX_mouse_controller import Mouse
elif system == 'linux2':
	print "platform: Linux2"
	from Linux_mouse_controller import Mouse
else:
	print "OS not supported, probably Windows ;)"

import curses
	
if __name__ == '__main__':

	STEP = 10

	m = Mouse()

	m.moveTo(500, 28)
	sleep(1)
	m.leftClick()
	m.leftButtonDown()
	sleep(1)
	for i in xrange(10):
		sleep(0.5)
		m.moveBy(5,5)
	m.leftButtonUp()
	sleep(1)
	for i in xrange(10):
		sleep(0.5)
		m.moveBy(5,10)
	m.rightClick()
	sleep(3)
	m.leftClick()
	for i in xrange(5):
		sleep(0.5)
		m.moveBy(-5,-10)
	for i in xrange(5):
		sleep(0.5)
		m.moveBy(-5,-5)
	m.leftButtonDown()
	sleep(1)
	for i in xrange(10):
		sleep(0.5)
		m.moveBy(5,5)
	m.leftButtonUp()

	#try:
		#stdscr = curses.initscr()
		#curses.cbreak()
		#stdscr.keypad(1)
#
		#stdscr.addstr(0,10,"Hit 'q' to quit")
		#stdscr.refresh()
#
		#key = ''
		#while key != ord('q'):
		    #key = stdscr.getch()
		    #stdscr.addch(20,25,key)
		    #print "size " + str(m.x) + " " + str (m.y) + " " + str(m.maxX) + " " + str(m.maxY)
		    #stdscr.refresh()
		    #if key == curses.KEY_UP: 
		        #stdscr.addstr(2, 20, "Up")
		        #m.moveBy(0, -STEP)	        
#
		    #elif key == curses.KEY_DOWN: 
		        #stdscr.addstr(3, 20, "Down")
		        #m.moveBy(0, STEP)
#
		    #elif key == curses.KEY_LEFT:
		    	#stdscr.addstr(4, 20, "Left")
		        #m.moveBy(-STEP, 0)
#
		    #elif key == curses.KEY_RIGHT:
		    	#stdscr.addstr(5, 20, "Right")
		        #m.moveBy(STEP, 0)
#
		    #elif key == ord(' '):
		    	#m.leftButtonDown()
#
		    #elif key == ord('b'):
		    	#m.leftButtonUp()
#
	#finally:
		#curses.endwin()

