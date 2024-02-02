lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

max_list = max(lists, key=len)
min_list = min(lists, key=len)

print("max_list", max_list)
print("min_list", min_list if max_list != min_list else None)
