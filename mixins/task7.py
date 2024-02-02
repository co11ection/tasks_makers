class ExtensionMixin:
    
    def add_extension(self, title: str) -> str:
        self.extensions.append(title)
        return f"Добавлено новое расширение {title} для игры {self.name}."
    

    def remove_extension(self, title: str) -> str:
        if title in self.extensions:
            self.extensions.remove(title)
            return f"{title} был отключен от {self.name}"
        
        return "Такого расширения нет в списке."


class Game(ExtensionMixin):

    def __init__(self, type: str, name: str) -> None:
        self.type = type
        self.name = name
        self.extensions = []


    def get_description(self, description: str) -> str:
        return f"{self.name} это {description}"


    def get_extensions(self) -> str:
        if self.extensions:
            return " ".join(self.extensions)

        return "Нет подключенных расширений"
