with open("task3.txt", "w+") as file_:
    for num in range(10):
        file_.write(f"{num}*")
    
    file_.seek(0)
    
    print(file_.read())
