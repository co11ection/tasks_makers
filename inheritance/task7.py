from datetime import datetime


class SmartPhones:

    def __init__(self, name: str, color: str, memory: int) -> None:
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = 0


    def __str__(self) -> str:
        return f"{self.name} {self.memory}"


    def charge(self, power: int) -> None:
        self.battery += power


class Iphone(SmartPhones):

    def __init__(self, name: str, color: str, memory: int, ios: str) -> None:
        super().__init__(name, color, memory)
        self.ios = ios


    def send_imessage(self, message: str) -> str:
        return f"sending {message} from {self}"


class Samsung(SmartPhones):

    def __init__(self, name: str, color: str, memory: int, android: str) -> None:
        super().__init__(name, color, memory)
        self.android = android


    def show_time(self) -> str:
        return datetime.now().time()


phone = SmartPhones("generic", "blue", "128GB")

print(phone)
print(phone.battery)
phone.charge(20)
print(phone.battery)

iphone7 = Iphone("Iphone 7", "gold", "128gb", "12.1.3")

print(iphone7)
print(iphone7.send_imessage("hello"))

samsung21 = Samsung("Samsung A21", "black", "256gb", "Oreo")

print(samsung21.show_time())
