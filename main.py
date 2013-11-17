import sys
from OSX_mouse_controller import Mouse


import curses
	
if __name__ == '__main__':

	STEP = 5

	m = Mouse(100, 100)

	try:
		stdscr = curses.initscr()
		curses.cbreak()
		stdscr.keypad(1)

		stdscr.addstr(0,10,"Hit 'q' to quit")
		stdscr.refresh()

		key = ''
		while key != ord('q'):
		    key = stdscr.getch()
		    stdscr.addch(20,25,key)
		    print "size " + str(m.x) + " " + str (m.y) + " " + str(m.maxX) + " " + str(m.maxY)
		    stdscr.refresh()
		    if key == curses.KEY_UP: 
		        stdscr.addstr(2, 20, "Up")
		        m.moveBy(0, -STEP)	        

		    elif key == curses.KEY_DOWN: 
		        stdscr.addstr(3, 20, "Down")
		        m.moveBy(0, STEP)

		    elif key == curses.KEY_LEFT:
		    	stdscr.addstr(4, 20, "Left")
		        m.moveBy(-STEP, 0)

		    elif key == curses.KEY_RIGHT:
		    	stdscr.addstr(5, 20, "Right")
		        m.moveBy(STEP, 0)

		    elif key == ord(' '):
		    	m.doubleRightClick()

	finally:
		curses.endwin()

