class Phone:

    def __init__(self, name: str, last_name: str, phone: str) -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone


    def get_info(self) -> None:
        info = f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}"
        print(info)


contact = Phone("John", "Snow", "+996707707707")
contact.get_info()
