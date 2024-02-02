list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] 
repeated = []

for num in list_:
    if list_.count(num) > 1 and num not in repeated:
        repeated.append(num)

print(repeated)
