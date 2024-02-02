from functools import reduce


list_ = [1, 2, 3, 4]
result = reduce(lambda num1, num2: num1 + num2, list_)

print(result)
