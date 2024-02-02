dict_ = {"key1": "value1", "key2": "value2"}

try:
    print(dict_["key1"])
except KeyError:
    print("Нет такого ключа!")
