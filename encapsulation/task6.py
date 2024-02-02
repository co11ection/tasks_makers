class Person:

    def __init__(self, name: str, phone_number, card_number) -> None:
        self.name = name
        self._phone_number = phone_number
        self.__card_number = card_number


john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")

print(john.name)
print(john._phone_number)
print(john._Person__card_number)
