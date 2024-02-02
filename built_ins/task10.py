from functools import reduce


list_ = ["Paul", "George", "Ringo", "John"]
result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)

print(result)
