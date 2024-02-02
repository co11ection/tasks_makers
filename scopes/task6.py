a = {"Мурат": 24, "Эржан": 21, "Чынгыз": 24, "Алтынай": 17, "Асема": 16}

for name, age in a.items():
    if age >= 17:
        print(f"{name}, Вы можете войти в клуб")
    else:
        print(f"{name}, извините, Вы не проходите по age-control")
