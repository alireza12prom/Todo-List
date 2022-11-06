from Lists.tasks import TasksList
from Tasks.task import Task

class ImportantList(TasksList):

    __instanc = None
    def __new__(cls, *args):
        if cls.__instanc is None:
            cls.__instanc = object.__new__(cls)
        return cls.__instanc

    def __init__(self, ID:str, name:str) -> None:
        super().__init__(ID, name)

    def view(self) -> None:
        for task in self._tasks + self._customs:
            if task.important:
                print(task)
        
    def add_task(self, task_name:str, task_des:str) -> Task:
        task = super().add_task(task_name, task_des)
        task.important = True
        return task

    def mark_as_important(self, ID: str) -> None:
        raise NotImplementedError

    @classmethod
    def _find_task_by_ID(cls, ID:str):
        tar = list(filter(lambda t: t.ID == ID and t.important, cls._tasks + cls._customs))
        return tar[0] if len(tar) != 0 else None
