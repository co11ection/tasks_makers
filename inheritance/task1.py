class Class1:
    
    def first(self) -> None:
        pass


    def second(self) -> None:
        pass


class Class2(Class1):

    def third(self) -> None:
        pass
    

    def fourth(self) -> None:
        pass


obj = Class2()

obj.first()
obj.second()
obj.third()
obj.fourth()
