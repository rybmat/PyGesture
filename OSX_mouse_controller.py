from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventRightMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGEventRightMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap, kCGEventLeftMouseDragged, kCGEventSourceStateHIDSystemState
from Quartz.CoreGraphics import CGEventCreate
from Quartz.CoreGraphics import CGEventGetLocation
from Quartz.CoreGraphics import CGEventSourceCreate
from AppKit import NSScreen, NSEvent

class Mouse():
    """a class containing attributes and methods needed to controlling mouse cursor
    """
    def __init__(self):
        self.maxX = int(NSScreen.mainScreen().frame().size.width)      
        self.maxY = int(NSScreen.mainScreen().frame().size.height)

        self.moveBy(0,0)


    def __mouseEvent(self, type, x, y):
        """creates and posts mouse event of given type at (posx, posy) position"""
        theEvent = CGEventCreateMouseEvent(CGEventSourceCreate(kCGEventSourceStateHIDSystemState), type, (x, y), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)


    def moveTo(self, x, y):
        """moves mouse cursor to (x,y) position"""

        if x < 0:
            self.x = 0
        elif x > self.maxX:
            self.x = self.maxX
        else:
            self.x = x

        if y < 0:
            self.y = 0
        elif y > self.maxY:
            self.y = self.maxY
        else:
            self.y = y 

        print self.x, self.y
        
        self.__mouseEvent(kCGEventMouseMoved, self.x, self.y)
        self.__mouseEvent(kCGEventLeftMouseDragged, self.x, self.y)


    def moveBy(self, x, y):
        """moves coursor by x step and y step"""
        ourEvent = CGEventCreate(None);
        mouseLocation = CGEventGetLocation(ourEvent);
        self.moveTo(int(mouseLocation.x) + x, int(mouseLocation.y) + y)

    

    def leftButtonDown(self):
        """makes left button of mouse pushed"""
        self.__mouseEvent(kCGEventLeftMouseDown, self.x, self.y)
       

    def leftButtonUp(self):
        """makes left button of mouse unpushed"""
        self.__mouseEvent(kCGEventLeftMouseUp, self.x, self.y)


    def leftClick(self):
        """makes "left click" """
        self.leftButtonDown()
        self.leftButtonUp()


    def doubleLeftClick(self):
        """ makes double left Click """
        self.leftClick()
        self.leftClick()

    

    def rightButtonDown(self):
        """makes right button of mouse pushed"""
        self.__mouseEvent(kCGEventRightMouseDown, self.x, self.y)


    def rightButtonUp(self):
        """makes right button of mouse unpushed"""
        self.__mouseEvent(kCGEventRightMouseUp, self.x, self.y)


    def rightClick(self):
        """makes "right click" """
        self.rightButtonDown()
        self.rightButtonUp()


    def doubleRightClick(self):
        """ makes double right Click """
        self.rightClick()
        self.rightClick()


