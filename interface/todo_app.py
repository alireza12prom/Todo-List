from abc import ABC, abstractclassmethod


class ITodoApplication(ABC):

    @abstractclassmethod
    def create_new_list(self):
        pass

    @abstractclassmethod
    def delete_list(self):
        pass
    
    @abstractclassmethod
    def rename_list(self):
        pass
    
    @abstractclassmethod
    def view(self):
        pass
    
    @abstractclassmethod
    def get_list(self):
        pass

