prairie_pirates = [
["Tractor Jack", 1000, True],
["Plowshare Pete", 950, False],
["Prairie Lily", 245, True],
["Red River Rosie", 350, True],
["Mad Athabasca McArthur", 842, False],
["Assiniboine Sally", 620, True],
["Thresher Tom", 150, True],
["Cranky Canola Carl", 499, False]
]

pirates = [[pirate[0], pirate[1]*42] for pirate in prairie_pirates if pirate[2]]

print(pirates)
