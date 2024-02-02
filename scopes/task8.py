def count_symbols(string: str) -> str:
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщъь"

    vowels_count = 0
    consonants_count = 0
    others_count = 0

    for symbol in string.lower():
        if symbol in vowels:
            vowels_count += 1
        elif symbol in consonants:
            consonants_count += 1
        else:
            others_count += 1
    
    result = f"Количество гласных: {vowels_count}, согласных: {consonants_count}, остальных символов: {others_count}"

    return result


print(count_symbols("Мурат супер!"))
