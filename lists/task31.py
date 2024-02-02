colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
result = []

for color in colors:
    result.append(color[::-1])

print(sorted(result, key=len))
