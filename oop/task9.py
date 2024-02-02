class Math():
    
    def __init__(self, number: int) -> None:
        self.number = number


    def get_factorial(self) -> int:
        result = 1

        for i in range(self.number):
            result *= i+1

        return result


    def get_sum(self) -> int:
        result = 0
        
        for digit in str(self.number):
            result += int(digit)
        
        return result


    def get_mul_table(self) -> str:
        result = ""

        for i in range(1, 11):
            multiply = self.number * i
            result += f"{self.number}x{i}={multiply}\n"
        
        return result


number = Math(11)

print(number.get_factorial())
print(number.get_sum())
print(number.get_mul_table())
