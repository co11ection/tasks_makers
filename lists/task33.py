lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
sums = []

for element in lists:
    sums.append(sum(element))

index = sums.index(max(sums))

print(lists[index])
