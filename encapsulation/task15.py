class Person:

    def __init__(self) -> None:
        self.__name = None
        self.__last_name = None
        self.__age = None
        self.__email = None


    def get_name(self) -> str:
        return self.__name


    def set_name(self, __name: str) -> None:
        self.__name = __name


    def get_last_name(self) -> str:
        return self.__last_name


    def set_last_name(self, __last_name: str) -> None:
        self.__last_name = __last_name


    def get_age(self) -> int:
        return self.__age


    def set_age(self,__age: int) -> None:
        self.__age = __age


    def get_email(self) -> str:
        return self.__email


    def set_email(self, __email: str) -> None:
        self.__email = __email


john = Person()

print(john.get_name())
print(john.get_last_name())
print(john.get_age())
print(john.get_email())

john.set_name("John")
john.set_last_name("Snow")
john.set_age(30)
john.set_email("johnsnow@gmail.com")

print(john.get_name())
print(john.get_last_name())
print(john.get_age())
print(john.get_email())
