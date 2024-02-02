class Person:

    def __init__(self, name: str, phone_number: int, card_number: int) -> None:
        self.name = name
        self._validate_phone_number(phone_number)
        self.__validate_card_number(card_number)


    def _validate_phone_number(self, phone_number: int) -> None:
        if type(phone_number) is int:
            if str(phone_number).startswith("996"):
                self._phone_number = phone_number
                return

        self._phone_number = None


    def __validate_card_number(self, card_number: int) -> None:
        if type(card_number) is int:
            if len(str(card_number)) == 16:
                self.__card_number = card_number
                return

        self.__card_number = None


tolik = Person("Anatoly", 996557551757, 9999999999999999)

print(tolik.name)
print(tolik._phone_number)
print(tolik._Person__card_number)
