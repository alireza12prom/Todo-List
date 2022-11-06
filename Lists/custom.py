from Lists.tasks import TasksList
from Tasks.task import Task
from Error.error import *


class CustomList(TasksList):

    def __new__(cls, *args):
        return object.__new__(cls)
    
    def __init__(self, ID: str, name: str) -> None:
        super().__init__(ID, name)
        self._tasks = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def view(self) -> None:
        return super().view()

    # Create/Delete a task
    def add_task(self, task_name: str, task_des: str) -> Task:

        # generate a random unique ID
        ID = self._random_id()

        # initializing
        new_task = Task(ID, task_name, task_des)
        
        # add tasks to private list
        self._tasks.append(new_task)
        return new_task

    def delete_task(self, ID: str) -> Task:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # remove task from public list
        if task in self._customs:
            self._customs.remove(task)
        
        # remove task from private list
        self._tasks.remove(task)

        # remove the task id from the bin
        CustomList._bin.remove(task.ID)
        return task


    # Mark as Done/Undone
    def mark_as_done(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        task.state = True

    def mark_as_undone(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError("Error: There is not task with this ID!")
        task.state = False


    # Mark as Important/ Not important
    def mark_as_important(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError("Error: There is no task with this ID!")
        
        task.important = True

        # shair this task with another todo list
        try:
            self._publish(task)
        except ApplicationCrashError as err:
            raise err
        
    def mark_as_notimportant(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError("Error: There is no task with this ID!")

        task.important = False


    # Add to/ Remove from my_day
    def add_to_myday(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # check if date already seted, raising error
        if task.date is not None:
            raise AlreadySetError
        task.date = self._tody_date()

        # shair this task with another todo lists
        try:
            self._publish(task)
        except ApplicationCrashError as err:
            raise err
        
    def remove_from_myday(self, ID: str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError

        if task.date == "":
            raise

        task.date = ""


    # remove all tasks from list
    def clear(self) -> None:
        for task in self._tasks:
            if task in CustomList._tasks:
                CustomList._tasks.remove(task)
        self._tasks.clear()

    def _find_task_by_ID(self, ID:str) -> Task: 
        """ return the instance of the task """

        tar = list(filter(lambda t: t.ID == ID, self._tasks))
        return tar[0] if len(tar) != 0 else None

    # this function adding a task to public list if there was not
    # for shairing task with another lists like Important, Myday, ....
    def _publish(self, task:Task,/) -> None:
        if not isinstance(task, Task):
            raise ApplicationCrashError

        if task in self._customs:
            return
        self._customs.append(task)