chars = ["a", "b", "c", "d", "e", "f", "g"]
merge_from = input()
merge_to = input()
from_to = "".join(chars[chars.index(merge_from):chars.index(merge_to) + 1])
result = []

for char in chars[:chars.index(merge_from)]:
    result.append(char)

result.append(from_to)

for char in chars[chars.index(merge_to) + 1:]:
    result.append(char)

print(result)
