from abc import ABC, abstractmethod


class Coder(ABC):
    count_code_time = 0

    @abstractmethod
    def get_info(self) -> None:
        pass


    @abstractmethod
    def coding(self) -> None:
        pass


class Backend(Coder):

    def __init__(self, experience: str, languages_backend: str) -> None:
        self.experience = experience
        self.languages_backend = languages_backend


    def coding(self, code_time: int) -> None:
        self.count_code_time += code_time
        
    
    def get_info(self) -> str:
        return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"


class Frontend(Coder):

    def __init__(self, experience: str, languages_frontend: str) -> None:
        self.experience = experience
        self.languages_frontend = languages_frontend


    def coding(self, code_time: int) -> None:
        self.count_code_time += code_time
    

    def get_info(self) -> str:
        return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"
    

class Fullstack(Backend, Frontend):
    pass


a = Backend("Junior", "Python")
b = Frontend("Middle", "Javascript")
c = Fullstack("Senior", "Python and JS")

a.coding(12)
b.coding(45)
c.coding(17)

print(a.get_info())
print(b.get_info())
print(c.get_info())
