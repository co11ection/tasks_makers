num = chr(int(input()))

if num.isalpha():
    print(f"Это буква \"{num}\"")
else:
    print(f"Это не буква, а символ \"{num}\"")
