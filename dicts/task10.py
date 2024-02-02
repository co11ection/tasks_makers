a = {"a": None, "b": 1, "c": 2, "d": None, "e": 3}

for key, value in a.copy().items():
    if not value:
        a.pop(key)

print(a)
