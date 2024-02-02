a = "12342342345" 
b = [1,["a",5,6],2,3,4,5] 
c = {1:"a", 2: {"a": 1, "b": 2}, 3:"c"} 
abc = (a, b, c)

for element in abc:
    print(len(element))
