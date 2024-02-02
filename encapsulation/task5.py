class Person:
    name = "John"
    _phone_number = "+996 557 55 17 57"
    __card_number = "9999 9999 9999 9999"


john = Person()

print(john.name)
print(john._phone_number)
print(john._Person__card_number)
