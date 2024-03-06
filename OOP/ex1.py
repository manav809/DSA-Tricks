import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        pi = math.pi
        return 2 * self.radius * pi
    def area(self):
        pi = math.pi
        return pi * (self.radius ** 2)
    
obj = Circle(2)
print(obj.area())
print(obj.circumference())
