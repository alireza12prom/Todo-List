import random
from Lists.tasks import TasksList
from Lists.custom import CustomList
from Lists.myday import MydayList
from Lists.important import ImportantList
from Error.error import TodolistNotFoundError, CantChangeDefaultListsError
from interface.todo_app import ITodoApplication

class TodoApplication(ITodoApplication):
    _bin = []
    def __init__(self, user_name):
        self.user_name = user_name
        self.__todoLists = []

    # initialize the default lists
    def setup(self) -> None:
        # initialize default todo lists
        tasks_list = TasksList("a", "Tasks")
        important_list = ImportantList("b", "Important")
        myday_list = MydayList("c", "Myday")

        # add to todo list
        self.__todoLists.append(tasks_list)
        self.__todoLists.append(important_list)
        self.__todoLists.append(myday_list)

    def view(self) -> None:
        for todo in self.__todoLists:
            print(todo)

    def create_new_list(self, name:str) -> CustomList:
        
        # generate a random unique ID
        ID = self._random_id()

        # create an instance and add it to todo lists
        new_list = CustomList(ID, name)
        self.__todoLists.append(new_list)
        
        # add new ID to bin
        self._bin.append(ID)

        return new_list

    def delete_list(self, ID:str) -> CustomList:

        # check ID that is true or no
        todo_list = self._find_list_by_ID(ID)
        if todo_list is None:
            raise TodolistNotFoundError

        # check the target list isn't a default list
        elif not isinstance(todo_list, CustomList):
            raise CantChangeDefaultListsError
        
        # clear list and remove all tasks in the list
        todo_list.clear()

        # delete list from todo lists
        self.__todoLists.remove(todo_list)

        # remove it's ID from bin
        self._bin.remove(todo_list.ID)
        return todo_list
    
    def rename_list(self, ID:str, new_name:str) -> None:
        # check ID that is true or no
        todo = self._find_list_by_ID(ID)
        if todo is None:
            raise TodolistNotFoundError

        # check the target list isn't a default list
        elif not isinstance(todo, CustomList):
            raise CantChangeDefaultListsError
        todo.name = new_name

    def get_list(self, ID:str) -> object:
        """ return the instance of the list """

        # check ID that is true or no
        todo = self._find_list_by_ID(ID)
        if todo is None:
            raise TodolistNotFoundError
        return todo

    def _random_id(self) -> str:
        while True:
            rand_num = random.randrange(1000, 9999)
            if str(rand_num) not in self._bin:
                break
        
        self._bin.append(str(rand_num))
        return str(rand_num)

    def _find_list_by_ID(self, ID:str):
        tar = list(filter(lambda l: l.ID == ID, self.__todoLists))
        return tar[0] if len(tar) != 0 else None

