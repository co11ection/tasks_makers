step = 3

list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
new_list = []

for iteration in range(step):
    inner_list = []

    for index in range(iteration, len(list_), step):
        inner_list.append(list_[index])

    new_list.append(inner_list)

print(new_list)
