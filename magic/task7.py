class Anagram(str):

    def __eq__(self, value: str) -> bool:
        return sorted(self) == sorted(value)


    def __mul__(self, num: int) -> str:
        return self[::-1] * num


word1 = Anagram("hello")
word2 = Anagram("olleh")

print(word1 == word2)
print(word1 * 3)
