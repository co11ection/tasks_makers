string = "pytohnist"
dict_ = {}

for symbol in string:
    dict_.update({symbol: string.count(symbol)})

print(dict_)
