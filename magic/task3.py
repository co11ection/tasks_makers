class MyList(list):

    def __getitem__(self, index: int):
        return super().__getitem__(index-1)


obj_list = MyList([1,2,3,4,5])

print(obj_list[1])
