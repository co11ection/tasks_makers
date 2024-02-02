dict1 = {"a": {"d": 1, "e": 4}, "b": {"f": 2, "j": 4}, "c": {"h": 3, "i": 9}}
dict2 = {}

for key, outer_value in dict1.items():
    result = 1

    for inner_value in outer_value.values():
        result *= inner_value

    dict2.update({key: result})
