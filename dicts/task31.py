dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

sorted_keys = sorted(dict_, key=dict_.get, reverse=True)

for key in sorted_keys:
    sorted_dict.update({key: dict_.get(key)})
