class Password:

    def __init__(self, password: str) -> None:
        self.password = password


    def __str__(self) -> str:
        encrypted_password = len(self.password) * "*"
        return encrypted_password


    def validate(self) -> str:
        if not 14 > len(self.password) > 8:
            raise Exception("Password should be longer than 8, and less than 15")

        SPECIALS = ("@", "#", "&", "$", "%", "!", "~", "*")

        nums_contain = False
        letters_contain = False
        specials_contain = False

        for symbol in self.password:
            if symbol.isdigit():
                nums_contain = True
            if symbol.isalpha():
                letters_contain = True
            if symbol in SPECIALS:
                specials_contain = True

        if not nums_contain:
            raise Exception("Password should contain numbers too")
        if not letters_contain:
            raise Exception("Password should contain letters as well")
        if not specials_contain:
            raise Exception("Your password should have some symbols")
        
        SUCCESS_MESSAGE = "Ваш пароль сохранен."

        return SUCCESS_MESSAGE


password = Password("joe@123456")

print(password)
