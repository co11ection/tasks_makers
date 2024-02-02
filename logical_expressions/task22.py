n = input()
phrase = f"На лугу пасется {n} коро"

if int(n) > 10 and int(n) < 15:
    print(phrase + "в")
elif n.endswith("1"):
    print(phrase + "ва")
elif n.endswith("2") or n.endswith("3") or n.endswith("4"):
    print(phrase + "вы")
else:
    print(phrase + "в")
