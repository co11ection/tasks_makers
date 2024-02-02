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

saved_amount = [round(reader[1] * 11.95, 2) for reader in SPL_Patrons]

print(saved_amount)
