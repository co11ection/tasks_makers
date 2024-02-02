class Word:

    def __new__(cls, string: str):
        modified_string = string.replace(" ", "")
        obj = super().__new__(cls)
        obj.string = modified_string

        return obj


    def __gt__(self, other) -> bool:
        return len(self.string) > len(other.string)


    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)


    def __ge__(self, other) -> bool:
        return len(self.string) >= len(other.string)


    def __le__(self, other) -> bool:
        return len(self.string) <= len(other.string)


word1 = Word("H e ll o")
word2 = Word("world!")

print(word1 > word2)
print(word1 < word2)
print(word1 >= word2)
print(word1 <= word2)
