inp1 = input().split()
list_ = []

for element in inp1:
    try:
        list_.append(int(element))
    except ValueError:
        raise ValueError("Данный элемент не является числом!")
