str_list = ['abc', 'xyz', 'aba', '1221']
indexs = []

for element in str_list:
    if element[0] == element[-1]:
        indexs.append(str_list.index(element))

print(indexs)
