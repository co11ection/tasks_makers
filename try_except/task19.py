num = 100000000

while num > 1:
    try:
        num -= 1
    except KeyboardInterrupt:
        print("Nope")
