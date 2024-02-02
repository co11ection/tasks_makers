SPL_Patrons = [
["Kim Tremblay", 134],
["Emily Wilson", 42],
["Jessica Smith", 215],
["Alex Roy", 151],
["Sarah Khan", 105],
["Samuel Lee", 220],
["William Brown", 24],
["Ayesha Qureshi", 199],
["David Martin", 56],
["Ajeet Patel", 69]
]

readers = [reader[0] for reader in SPL_Patrons if reader[1] > 100]

print(readers)
