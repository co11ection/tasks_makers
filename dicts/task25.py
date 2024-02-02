dict_ = {"Bootcamp": 8, "Makers": 6, "coding": 6, "hello": 5}
result = []
target = 0

for key, value in dict_.items():
    if value == target:
        result.append(key)
    elif value > target:
        target = value
        result.clear()
        result.append(key)

for element in result:
    print(element)
