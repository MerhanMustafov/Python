from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_area (self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

     
