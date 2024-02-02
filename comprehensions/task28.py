dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
list_ = [key.upper() for key, value in dict_.items() if value in range(200, 5001)]

print(list_)
