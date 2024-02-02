a = {"a": 1, "b": 5, "c": 4, "d": 3}
dict_ = {key: list(range(1, value+1)) for key, value in a.items()}

print(dict_)
