from datetime import datetime


class CreateMixin:

    def create(self, key, todo) -> None | str:
        if self.todos.get(key):
            return "Задача под таким ключом уже существует"

        self.todos.update({key: todo})
        return self.todos


class DeleteMixin:

    def delete(self, key) -> str:
        return self.todos.pop(key)


class UpdateMixin:

    def update(self, key, new_value) -> None:
        self.todos.update({key: new_value})
        return self.todos


class ReadMixin:

    def read(self) -> list:
        result = []

        for key in sorted(self.todos):
            result.append((key, self.todos[key]))

        return result


class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}


    def set_deadline(self, date: str) -> int:
        deadline = datetime.strptime(date, '%d/%m/%Y')
        today = datetime.today()
        days_left = (deadline - today).days + 1

        return days_left
