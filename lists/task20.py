list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
res = 0

for element in list_:
    if type(element) is int:
        res += element
    elif element.isdigit():
        res += int(element)

print(res)
