x = int(input())
y = int(input())

if remainder := (x % y):
    print("x не делится на y")
    print(f"Частное: {x // y}")
    print(f"Остаток: {remainder}")
else:
    print("x делится на y")
    print(f"Частное: {x // y}")
