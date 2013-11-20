from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventRightMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGEventRightMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGDisplayMoveCursorToPoint
from Quartz.CoreGraphics import CGDisplayShowCursor
from Quartz.CoreGraphics import CGWarpMouseCursorPosition
from Quartz.CoreGraphics import CGAssociateMouseAndMouseCursorPosition
from AppKit import NSScreen


class Mouse():
    """a class containing attributes and methods needed to controlling mouse cursor
    """
    def __init__(self, x=100, y=100):
        self.maxX = int(NSScreen.mainScreen().frame().size.width)      
        self.maxY = int(NSScreen.mainScreen().frame().size.height)
        CGAssociateMouseAndMouseCursorPosition(True)

        if (x in range(0, self.maxX)) and (y in range(0, self.maxY)):
            self.moveTo(x, y)
        else:
            self.moveTo(0, 0)

    def __mouseEvent(self, type, x, y):
        """creates mouse event of given type at (posx, posy) position"""
        theEvent = CGEventCreateMouseEvent(None, type, (x, y), kCGMouseButtonLeft)
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
        
        #self.__mouseEvent(kCGEventMouseMoved, self.x, self.y)
        CGDisplayMoveCursorToPoint (0, (x, y))
        #CGWarpMouseCursorPosition((x,y))
        CGDisplayShowCursor(0)


    def moveBy(self, x, y):
        """moves coursor by x step and y step"""
        self.moveTo(self.x + x, self.y + y)

    

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
        self.rightClick()
        self.rightClick()


