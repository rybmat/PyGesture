#-*- coding: utf-8 -*-
import autopy


class Mouse(): 
	"""a class containing attributes and methods needed to controlling mouse cursor"""
	def __init__(self, x=100, y=100):
		self.maxX, self.maxY=autopy.screen.get_size()
        
		if (x in range(0, self.maxX)) and (y in range(0, self.maxY)):
			self.moveTo(x, y)
		else:
			self.moveTo(0, 0)

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

        #print self.x, self.y
		autopy.mouse.move(self.x,self.y)
       


	def moveBy(self, x, y):
		"""moves coursor by x step and y step"""
		self.moveTo(self.x + x, self.y + y)
	
	def leftButtonDown(self):
		"""makes left button of mouse pushed"""
		autopy.mouse.toggle(True,autopy.mouse.LEFT_BUTTON)


	def leftButtonUp(self):
		"""makes left button of mouse unpushed"""
		autopy.mouse.toggle(False,autopy.mouse.LEFT_BUTTON)

	def leftClick(self):
		self.leftButtonDown()
		self.leftButtonUp()

	def doubleLeftClick(self):
		self.leftClick()
		self.leftClick()

	def rightButtonDown(self):
		"""makes right button of mouse pushed"""
		autopy.mouse.toggle(True,autopy.mouse.RIGHT_BUTTON)

	def rightButtonUp(self):
		"""makes right button of mouse unpushed"""
		autopy.mouse.toggle(False,autopy.mouse.RIGHT_BUTTON)
	
	def rightClick(self):
		self.rightButtonDown()
		self.rightButtonUp()

	def doubleRightClick(self):
		self.rightClick()
		self.rightClick()

