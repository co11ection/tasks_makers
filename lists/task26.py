colors1 = ["red", "orange", "green", "blue", "white"]
colors2 = ["black", "yellow", "green", "blue"]

c1c2_diff = []
c2c1_diff = []

for color in colors1:
    if not color in colors2:
        c1c2_diff.append(color)

for color in colors2:
    if not color in colors1:
        c2c1_diff.append(color)

print(c1c2_diff, c2c1_diff)
