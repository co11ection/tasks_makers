list_ = [1, 2, 3, 4, 5]
new_list = []

for num in list_:
    new_list.append("нечетное" if num % 2 else "четное")

print(new_list)
