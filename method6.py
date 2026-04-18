import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_circle_ares(self):
        return math.pi*self.radius**2
    def calculate_circle_perimeter(self):
        return 2*math.pi*self.radius
radius=float(input("input the radius of the circle:"))
cob=Circle(radius)
area=cob.calculate_circle_ares()
perimeter=cob.calculate_circle_perimeter()
print("Area of the circle:",area)
print("perimeter of the circle:",perimeter)
