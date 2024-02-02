my_dict = {"first": {"a": 1}, "second": {"b": 2}} 
dict_ = {key: inner_value for key, value in my_dict.items() for inner_value in value.values()}

print(dict_)
