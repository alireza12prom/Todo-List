from Lists.tasks import TasksList
from Tasks.task import Task

class MydayList(TasksList):

    __instanc = None
    def __new__(cls, *args):
        if cls.__instanc is None:
            cls.__instanc = object.__new__(cls)
        return cls.__instanc
    
    def __init__(self, ID:str, name:str) -> None:
        super().__init__(ID, name)

    def view(self) -> None:
        for task in self._tasks + self._customs:
            if task.date is not None:
                print(task)

    def add_task(self, task_name:str, task_des:str) -> Task:
        task =  super().add_task(task_name, task_des)
        task.date = self._tody_date()
        return task

    def add_to_myday(self, ID: str):
        raise NotImplementedError

    @classmethod
    def _find_task_by_ID(cls, ID):
        tar = list(filter(lambda t: t.ID == ID and t.date is not None, cls._tasks + cls._customs))
        return tar[0] if len(tar) != 0 else None
