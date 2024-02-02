dict_ = {"a": {"e": 32}, "b": {"f": 36}, "c": {"j": 37}, "d": {"h": 21}}

for key, outer_value in dict_.copy().items():
    inner_value = list(outer_value.values())[0]
    dict_.update({key: inner_value})
