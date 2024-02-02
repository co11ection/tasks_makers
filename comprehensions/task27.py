list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude" ] 
dict_ = {element: len(element)**2 for element in list_name if len(element) > 4}

print(dict_)
