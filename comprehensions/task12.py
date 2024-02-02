dict_ = {"first": 1, "second": 2, "third": 3}
a = {key: "even" if not value % 2 else "odd" for key, value in dict_.items()}

print(a)
