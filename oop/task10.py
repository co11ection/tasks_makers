class ToDo:
    instances = {}


    def __init__(self, task: str) -> None:
        self.task = task


    @classmethod
    def list_of_tasks(cls) -> dict:
        result = []
        sorted_priorities = sorted(cls.instances)

        for priority in sorted_priorities:
            result.append((priority, cls.instances[priority]))

        return result


    def give_priority(self, priority: int) -> None:
        self.__class__.instances.update({priority: self.task})


movies = ToDo("сходить в кино")
movies.give_priority(3)
homework = ToDo("сделать домашку")
homework.give_priority(1)
walk = ToDo("выгулять собаку")
walk.give_priority(2)

print(ToDo.list_of_tasks())
