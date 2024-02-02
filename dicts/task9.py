a = {"a": 1, "b": 4, "c": 1, "d": 5, "e": 6}
b = {}

for key, value in a.items():
    b.update({key: value if value % 2 else 2})

print(b)
