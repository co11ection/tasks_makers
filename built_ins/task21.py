list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]

l1 = list(filter(lambda x: x > 0, list_))
l2 = list(filter(lambda x: x <= 0, list_))

print(list(zip(l1, l2)))
