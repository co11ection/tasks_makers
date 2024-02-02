list_ = ["hello", 23, 56, "world", 928, "Makers", 456, "word", 223, 89, "bootcamp", "coding"]
list_of_str = []
list_of_int = []

for element in list_:
    if type(element) is str:
        list_of_str.append(element)
    
    if type(element) is int:
        list_of_int.append(element)

dict_ = dict(zip(list_of_str, list_of_int))
