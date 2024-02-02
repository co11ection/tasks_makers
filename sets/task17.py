set1 = {i for i in range(10) if not i % 2}
set2 = {i for i in range(10) if i % 2}

print("Множества пересекаются!" if set1 & set2 else "Множества не пересекаются!")
