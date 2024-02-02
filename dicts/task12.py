a = {"apple": 2, "orange": 5, "banana": 10}

for key, value in a.copy().items():
    if not value % 2:
        a.pop(key)

print(a)
