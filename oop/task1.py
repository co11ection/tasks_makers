class Song:
    
    def __init__(self, author: str, title: str, year: int) -> None:
        self.author = author
        self.title = title
        self.year = year
    

    def show_author(self) -> str:
        info = f"Автор этой песни {self.author}"
        return info


    def show_title(self) -> str:
        info = f"Название этой песни {self.title}"
        return info


    def show_year(self) -> str:
        info = f"Эта песня вышла в {self.year} году"
        return info


song = Song("Pharrell Williams", "Happy", 2013)

print(song.show_title())
print(song.show_author())
print(song.show_year())
