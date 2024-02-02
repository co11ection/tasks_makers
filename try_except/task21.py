inp1 = input()
inp2 = input()

try:
    print(int(inp1) + int(inp2))
except ValueError:
    print(str(inp1) + str(inp2))
