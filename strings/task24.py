string1 = "America"
string2 = "Japan"
result = ""
result += string1[0] + string2[0]
result += string1[len(string1) // 2] + string2[len(string2) // 2]
result += string1[-1] + string2[-1]

print(result)
