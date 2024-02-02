class Person:

    def __init__(self) -> None:
        self.__name = None
        self.__last_name = None
        self.__age = None
        self.__email = None


    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, __name: str) -> None:
        self.__name = __name


    @property
    def last_name(self) -> str:
        return self.__last_name


    @last_name.setter
    def last_name(self, __last_name: str) -> None:
        self.__last_name = __last_name


    @property
    def age(self) -> int:
        return self.__age


    @age.setter
    def age(self,__age: int) -> None:
        self.__age = __age


    @property
    def email(self) -> str:
        return self.__email


    @email.setter
    def email(self, __email: str) -> None:
        self.__email = __email


john = Person()

print(john.name)
print(john.last_name)
print(john.age)
print(john.email)

john.name = "John"
john.last_name = "Snow"
john.age = 30
john.email = "johnsnow@gmail.com"

print(john.name)
print(john.last_name)
print(john.age)
print(john.email)
