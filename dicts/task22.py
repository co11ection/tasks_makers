dict_ = {"a": None, "b": 1, "c": 2, "d": None, "e": 3}

for key, value in dict_.copy().items():
    if value:
        dict_.pop(key)
