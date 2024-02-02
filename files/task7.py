def longest_words(filename: str) -> list:
    result = []
    max_length = 0

    with open(filename, "r") as file_:
        lines = file_.readlines()

        for line in lines:
            words = line.split()

            for word in words:
                if len(word) > max_length:
                    max_length = len(word)
                    result = [word]
                elif len(word) == max_length:
                    result.append(word)

        if len(result) == 1:
            print(result[0])
        else:
            print(result)
