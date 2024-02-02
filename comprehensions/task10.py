n = int(input())
dict_ = {num: num**2 for num in range(1, 500) if not num % n}

print(dict_)
