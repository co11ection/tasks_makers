dict1 = {25: "apple", 26: "orange", 27: "banana"}
dict2 = {}

for key, value in dict1.items():
    dict2.update({key**2: value})
