def filter_comment(comment: str, banlist=[]) -> None:
    modified_comment = comment.replace(".", "").replace("!", "").replace("?", "").replace(",", "").lower().split()
    
    for word in modified_comment:
        if word in banlist:
            raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
