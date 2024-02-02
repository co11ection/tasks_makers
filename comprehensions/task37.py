dict_ = {num: str(num) for num in range(10)}
dict_ = {key: len(value)**3 if key % 2 else len(value) for key, value in dict_.items()}

print(dict_)
