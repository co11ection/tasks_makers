name_of_list = ["Helloworld!"]
string = name_of_list[0]
half_length = len(string) // 2

if len(string) % 2:
    half_length += 1

new_list = []
new_list += string[half_length:] + string[:half_length]

print(new_list)
