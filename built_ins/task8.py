list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

list2 = len(list(filter(lambda x: not x % 2, list_)))
list3 = len(list(filter(lambda y: y % 2, list_)))

result = f"even: {list2}, odd: {list3}"

print(result)
