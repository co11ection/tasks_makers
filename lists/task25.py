list_ = ["sun", "flowers", "rumor", "stranger", "adventure", "architect", "accompany", "abandon", "cartoon"]

search = input()
result = []

for element in list_:
    if element.startswith(search):
        result.append(element)

print(result)
