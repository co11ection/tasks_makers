list_ = [1, 4, 9, 16, 25, 36] 

try:
    print(list_[6])
except IndexError:
    print("Нет такого элемента!")
