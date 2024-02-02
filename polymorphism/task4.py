from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    
    @abstractmethod
    def get_area(self) -> None:
        pass


class Triangle(Shape):
    
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
    

    def get_area(self) -> float:
        area = self.base / 2 * self.height
        return area


class Square(Shape):

    def __init__(self, length: float) -> None:
        self.length = length


    def get_area(self) -> float:
        area = self.length**2
        return area


class Circle(Shape):

    def __init__(self, radius: float) -> None:
        self.radius = radius


    def get_area(self) -> float:
        area = pi * self.radius**2
        return area


triangle = Triangle(25, 1)
square = Square(5)
circle = Circle(10)

print(triangle.get_area())
print(square.get_area())
print(circle.get_area())
