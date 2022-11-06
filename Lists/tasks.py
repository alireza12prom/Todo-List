import random, time
from interface.todo_list import ITodoList
from Tasks.task import Task
from Error.error import AlreadySetError, TaskNotFoundError


class TasksList(ITodoList):
    _tasks = []     # default lists added their tasks here
    _customs = []   # custom lists added their tasks here
    _bin = []       # it contains with the useage id

    # for making sure that the class create same objects in each initializing
    __instanc = None
    def __new__(cls, *args):
        if cls.__instanc is None:
            cls.__instanc = object.__new__(cls)
        return cls.__instanc

    def __init__(self, ID:str, name:str) -> None:
        self._ID = ID
        self._name = name

    def __str__(self):
        return "{}. {}".format(self._ID, self._name)

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name

    def view(self) -> None:
        for task in self._tasks:
            print(task)

    def add_task(self, task_name:str, task_des:str) -> Task:
        # make a random ID
        ID = self._random_id()
        
        # create an instance
        new_task = Task(ID, task_name, task_des)
        
        # save new task 
        TasksList._tasks.append(new_task)
        
        # save their ID to bin
        self._bin.append(ID)

        return new_task

    def remove_task(self, ID:str) -> Task:
        
        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # remove task from tasks list
        self._tasks.remove(task)

        # remove task ID from bin
        TasksList._bin.remove(task.ID)

        return task

    def mark_as_done(self, ID:str) -> None:
        
        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # change the state of the task to True
        task.state = True

    def mark_as_undone(self, ID:str) -> None:
        
        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # change the state of the task to False
        task.state = False
    
    def mark_as_important(self, ID:str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # change the state of the task
        task.important = True

    def mark_as_notimportant(self, ID:str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError

        # change the state of the task
        task.important = False
    
    def add_to_myday(self, ID:str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # if the task has a date, it means it is already added in myday
        elif task.date is not None:
            raise AlreadySetError
        
        # set today date to task date
        task.date = self._tody_date()
    
    def remove_from_myday(self, ID:str) -> None:

        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError
        
        # if the task hasn't any date, it means it isn't in myday
        if task.date is None:
            raise

        task.date = None

    def get_task(self, ID:str) -> Task:
        """ return the instance of the task """
        
        # check ID that is true or no
        task = self._find_task_by_ID(ID)
        if task is None:
            raise TaskNotFoundError

        return task

    @classmethod
    def _random_id(cls) -> str:
        """ This function generate a unique random ID """

        while True:
            rand_num = random.randrange(1000, 9999)
            if rand_num not in cls._bin:
                cls._bin.append(str(rand_num))
                return str(rand_num)

    @classmethod
    def _find_task_by_ID(cls, ID:str):
        tar = list(filter(lambda t: t.ID == ID, cls._tasks))
        return tar[0] if len(tar) != 0 else None
    
    @staticmethod
    def _tody_date():
        """ return the date to format d/m/y """
        return time.strftime("%d/%m/%Y")

