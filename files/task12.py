def filter_text(text_filename: str) -> str:
    with open(text_filename, "r") as file_:
        source_text = file_.read()

    with open("forbidden_words.txt", "r") as file_:
        forbidden_words = file_.read().split()

    modified_text = source_text

    for word in forbidden_words:
        modified_text = modified_text.lower().replace(word, "*" * len(word))
    
    result = ""
    
    for ind in range(len(source_text)):
        if modified_text[ind] != "*":
            result += source_text[ind]
        else:
            result += "*"

    return result
