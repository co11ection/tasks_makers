list_ = ["123hello@gmail.com", "123", "hello"]

print(list(map(lambda x: x if x.endswith("@gmail.com") else "Not valid email", list_)))
