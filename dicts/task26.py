dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dict2 = {}

for key, value in dict1.items():
    dict2.update({key: value**3})
