from interface.todo_task import ITask

class Task(ITask):
    def __init__(self, ID:str, title:str, description:str=None, date:str=None) -> None:
        self._ID = ID
        self._title = title
        self._description = description
        self._date = date
        self._state = False
        self._important = False
    
    def __str__(self):
        return "{}{} {}. {}    {}".format(
            "*" if self._important else " ",
            "D" if self._state else "U", 
            self._ID, 
            self._title, 
            self._date if self._date is not None else "")

    @property
    def ID(self):
        return self._ID

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, val):
        self._title = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        self._date = val

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, val):
        self._state = val

    @property
    def important(self):
        return self._important

    @important.setter
    def important(self, val):
        self._important = val

