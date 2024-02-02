a = [set(), set(), set()]

inp1 = input()
inp2 = int(input())

for element in a:
    if a.index(element) == inp2-1:
        element.add(inp1)
    else:
        element.add("default value")

print(a)
