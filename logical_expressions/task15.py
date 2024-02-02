string = "123123"
res1 = 0
res2 = 0

for i in string[:3]:
    res1 += int(i)

for i in string[3:]:
    res2 += int(i)

print("да" if res1 == res2 else "нет")
