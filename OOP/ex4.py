import math

class Shape:
    def area():
        pass
    def perimeter():
        pass

class Triangle(Shape):
    def __init__(self, arc1, arc2, height):
        self.arc1 = arc1
        self.arc2 = arc2
        self.height = height
    def area(self):
        return 0.5 * self.arc1 * self.height
    def perimeter(self):
        return float(self.arc1 + self.arc2 + self.hypotenuse())
    
    def hypotenuse(self): 
        a_squared = self.arc1 ** 2
        b_squared = self.arc2 ** 2
        c_squared = a_squared + b_squared
        return math.sqrt(c_squared)
    
triangle = Triangle(1, 2, 2)
print("Triangle's Area: ", triangle.area())
print("Triangle's Perimeter: ", triangle.perimeter())

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return math.pi * self.diameter

circle = Circle(4)
print("Circle's Area: ", circle.area())
print("Circle's Perimeter: ", circle.perimeter())

class Square(Shape):
    def __init__(self, side1):
        self.side1 = side1
    def area(self):
        return self.side1 ** 2
    def perimeter(self):
        return self.side1 * 4

square = Square(2)
print("Square's Area: ", square.area())
print("Square's Perimeter: ", square.perimeter())

class Rectangle(Square):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return self.side1 * self.side2
    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2
    
rectangle = Rectangle(2, 3)
print("Rectangle's Area: ", rectangle.area())
print("Rectangle's Perimeter: ", rectangle.perimeter())
