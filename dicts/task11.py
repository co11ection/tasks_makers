a = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

for key, value in a.items():
    a.update({key: value / 5})

print(a)
