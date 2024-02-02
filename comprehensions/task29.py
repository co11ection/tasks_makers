dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict2 = {key.replace("i", ""): key.count("i") for key in dict1.keys()}

print(dict2)
