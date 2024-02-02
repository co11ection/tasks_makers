class MyNumber(int):

    def __init__(self, value: int) -> None:
        self.value = value


    def __add__(self, value: int) -> int:
        result = f"Это сложение и результат равен: {self.value + value}"
        return result


    def __sub__(self, value: int) -> int:
        result = f"Это вычитание и результат равен: {self.value - value}"
        return result


    def __mul__(self, value: int) -> int:
        result = f"Это умножение и результат равен: {self.value * value}"
        return result


    def __truediv__(self, value: int) -> float:
        result = f"Это деление и результат равен: {self.value / value}"
        return result


obj_int = MyNumber(5)

print(obj_int + 5)
print(obj_int - 5)
print(obj_int * 5)
print(obj_int / 5)
