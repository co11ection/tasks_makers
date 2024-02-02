class Person:

    def __init__(self, name: str, phone_number, card_number) -> None:
        self.__validate_name(name)
        self._phone_number = phone_number
        self.__card_number = card_number


    def __validate_name(self, name: str) -> None:
        if len(name) < 2:
            self.name = "John"
            return
        
        self.name = name.title()


sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")

print(sam.name)
print(sam._phone_number)
print(sam._Person__card_number)
