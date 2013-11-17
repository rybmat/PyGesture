# poniżej masz szkielet klasy odpowiedzialnej za obsługę myszki. Znajdź jakąś bibliotekę
# i zrób obsługę myszki pod linuxem (polecam autopy - niby na wszystkie platformy, ale
# na makach nie śmiga - coś z openGL-em poknocili i nie chce się kompilować). 
# Nie zmieniaj nazw publicznych metod i pól, żeby w głównym programie można było
# korzystać z tego samego kodu dla obu systemów
# jak chcesz zrobić metodę lub pole prywatne to nazwę zacznij od dwóch podkreślników
# np. 
#   self.__pole 
# albo 
#   def __metoda


class Mouse(): 
    """a class containing attributes and methods needed to controlling mouse cursor
    """
    def __init__(self, x=100, y=100):
        #self.maxX =    pobierz szerokość i wysokość ekranu i przypisz do tych pól  
        #self.maxY =
        

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
        #TODO - coś co spowoduje przesunięcie kursora na pozycję self.x, self.y
       


    def moveBy(self, x, y):
        """moves coursor by x step and y step"""
        self.moveTo(self.x + x, self.y + y)

    

    def leftButtonDown(self):
        """makes left button of mouse pushed"""
        #TODO
        pass


    def leftButtonUp(self):
        """makes left button of mouse unpushed"""
        #TODO
        pass


    def leftClick(self):
        """makes "left click" """
        self.leftButtonDown()
        self.leftButtonUp()


    def doubleLeftClick(self):
        self.leftClick()
        self.leftClick()

    

    def rightButtonDown(self):
        """makes right button of mouse pushed"""
        #TODO
        pass


    def rightButtonUp(self):
        """makes right button of mouse unpushed"""
        #TODO
        pass


    def rightClick(self):
        """makes "right click" """
        self.rightButtonDown()
        self.rightButtonUp()


    def doubleRightClick(self):
        self.rightClick()
        self.rightClick()


