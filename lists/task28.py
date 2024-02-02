list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
repeats = 3
res = []

for num in list_:
    if list_.count(num) >= repeats and num not in res:
        res.append(num)
    
print(res)
