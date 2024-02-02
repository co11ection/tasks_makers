list_ = ['a', 'n', 'n', 'a']
result = map(lambda ind: list_[ind] == list_[-ind-1], range(len(list_)))

print("NO" if False in result else "YES")
