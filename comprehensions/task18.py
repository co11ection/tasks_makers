list1 = [1, 2, "hello", 3, "world", 4, 5, "book", "code", 6, "Makers", 7, 8, 9, 10]
list2 = [element for element in list1 if type(element) is str]

print(list2)
