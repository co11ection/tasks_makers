names = ["rauchel", "john", "peter", "jessica", "steven123", "dandy34", "kamest", "potter"]

print(list(map(lambda name: f"{name} Python" if len(name) > 5 else f"{name} JavaScript", names)))
