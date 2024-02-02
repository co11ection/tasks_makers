class Circle:
    color = "Синий"
    pi = 3.14


    def __init__(self, radius: float) -> None:
        self.radius = radius


    def get_area(self) -> float:
        result = self.pi * self.radius**2
        return result


circle = Circle(2)
circle.color = "Зеленый"

print(circle.color)
print(circle.get_area())
