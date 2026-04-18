import math
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width 
    def calculate_Rectangle_ares(self):
        return self.length*self.width
    def calculate_Rectangle_perimeter(self):
        return 2*(self.length + self.width)
length=float(input("input the length:"))
width=float(input("input the width:"))
rob=Rectangle(length,width)
area=rob.calculate_Rectangle_ares()
perimeter=rob.calculate_Rectangle_perimeter()
print("Area of the rectangle:",area)
print("perimeter of the Rectangle:",perimeter)
