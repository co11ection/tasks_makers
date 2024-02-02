with open("task5.txt", "r") as file_:
    list_ = []

    for num in file_.readlines():
        list_.append(int(num))

    max_num = max(list_)
    min_num = min(list_)


with open("task6.txt", "w") as file:
    file.write(f"{min_num}-{max_num}")
