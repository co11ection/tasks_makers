num1 = input()
num2 = input()

try:
    print(int(num1) + int(num2))
except ValueError:
    print("Введите число!")
