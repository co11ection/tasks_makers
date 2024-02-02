tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
cleared_tuples = []

for element in tuples:
    if element:
        cleared_tuples.append(element)
    
print(cleared_tuples)
