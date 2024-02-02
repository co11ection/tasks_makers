dict_ = {
    "math": {
        "sum": sum
    },
    "vars": {
        "a": 5,
        "b": 20,
        "c": 50
    }
}

print(dict_["math"]["sum"](dict_["vars"].values()))
