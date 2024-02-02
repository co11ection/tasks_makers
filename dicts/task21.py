dict1 = {"a": 3, "b": 4, "c": 9, "d": 5, "e": 6}
dict2 = {}

for key, value in dict1.items():
    dict2.update({key: 1 if value % 2 else value})
