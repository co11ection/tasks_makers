set1 = {num for num in range(10)}
set2 = {num for num in range(8, 18)}
full_set = set1 | set2
repeats = 20 - len(full_set)

if repeats:
    print(f"В этом сете было {repeats} повторения, его длина составляет {20 - repeats}")
else:
    print("Ваш объединенный сет полностью уникальный!")
