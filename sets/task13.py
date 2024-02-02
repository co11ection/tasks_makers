robert = {5, 7, 11, 10, 28} 
kail = {1, 5, 14, 8, 22} 
merri = {19, 20, 3, 11, 10}
result = ""

if robert & kail:
    result += "kail"

if robert & merri:
    if result:
        result += " "

    result += "merri"

print(result if result else "no one")
