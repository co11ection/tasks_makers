list_ = [False, True, False, True, False, True, False, True, False, True]
new_list = [1 if element else 0 for element in list_]

print(new_list)
