class AreaSquare:
    def __init__(self,l):
        self.length = l
        
    def area_sq(self):
        print("area of square is: ", self.length*self.length)
        
        
class AreaRectangle(AreaSquare):
    def __init__(self, l, b):
        super().__init__(l)
        self.breadth = b
    def area_rect(self):
        print("area of rectangle is: ",self.length*self.breadth)
        
length = int(input("enter the length: "))
breadth = int(input("enter the breadth: "))

a = AreaRectangle(length, breadth)
a.area_sq()
a.area_rect()


