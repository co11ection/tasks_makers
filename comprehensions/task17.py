list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [num if num >= 0 else 1 for num in list_]

print(int_list)
