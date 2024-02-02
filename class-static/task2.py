class User:

    def __init__(self, name: str, lastname: str, email: str) -> None:
        self.name = name
        self.lastname = lastname
        self.email = email


    @staticmethod
    def validate_email(email) -> bool:
        result = "@" in email
        return result


    def __str__(self) -> str:
        if self.validate_email(self.email):
            return f"{self.name}: {self.email}"
        
        return "email в неправильном формате"


    @classmethod
    def create_user(cls, data: str):
        data_elements = data.split(", ")
        name = data_elements[0]
        lastname = data_elements[1]
        email = data_elements[2]
        user = cls(name, lastname, email)

        return user


user1 = User.create_user("John, Snow, john@email.com")
user2 = User.create_user("John, Snow, johnemail.com")

print(user1)
print(user2)
