a = int(input())
b = int(input())
c = int(input())

if a < b:
    if b < c:
        print(a, b, c)
    elif c < a:
        print(c, a, b)
    else:
        print(a, c, b)
elif a < c:
    print(b, a, c)
elif c < b:
    print(c, b, a)
else:
    print(b, c, a)
