num1 = int(input())
num2 = int(input())

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("На ноль делить нельзя")
    