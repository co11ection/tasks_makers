a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (b + c > a) and (c + a > b):
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        print("rectangular")
    elif (a**2 + b**2 < c**2) or (b**2 + c**2 < a**2) or (c**2 + a**2 < b**2):
        print("obtuse")
    elif (a**2 + b**2 > c**2) or (b**2 + c**2 > a**2) or (c**2 + a**2 > b**2):
        print("acute")
else:
    print("impossible")
