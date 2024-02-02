def func18(ints_and_strs: list) -> None:
    int_list = []
    str_list = []

    for element in ints_and_strs:
        if type(element) is int:
            int_list.append(element)
        
        if type(element) is str:
            str_list.append(element)
        
    return int_list, str_list
