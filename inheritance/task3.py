class MyString(str):

    def append(self, extra_string: str) -> None:
        self.mutable_string = self + extra_string


    def pop(self) -> str:
        last_char = self.mutable_string[-1]
        self.mutable_string = self.mutable_string[:-1]

        return last_char


    def __str__(self) -> str:
        return self.mutable_string


example = MyString("String")

example.append("hello")
print(example.pop())
print(example)
