from functools import reduce


list_ = [5, 6, 7, 8] 
result = reduce(lambda a, b: a * b, list_)

print(result)
