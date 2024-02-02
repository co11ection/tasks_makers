from functools import reduce


list_ = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x if x < y else y, list_))
