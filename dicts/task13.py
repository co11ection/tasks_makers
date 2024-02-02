a = {"a": 1, "b": 2, "c": 3}

for key, value in a.copy().items():
    a.pop(key)
    a.update({value: key})

print(a)
