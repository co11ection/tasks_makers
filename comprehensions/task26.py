dict_ = {"a": {"d": 3, "e": 45}, "b": {"f": 23, "j": 9}, "c": {"h": 12, "i": 89}}
list_ = [value for dictionary in dict_.values() for value in dictionary.values()]

print(list_)
