from abc import ABC, abstractmethod


class ITodoList(ABC):
    
    @abstractmethod
    def add_task(self):
        pass
    
    @abstractmethod
    def remove_task(self):
        pass

    @abstractmethod
    def mark_as_done(self):
        pass
    
    @abstractmethod
    def mark_as_undone(self):
        pass
    
    @abstractmethod
    def mark_as_important(self):
        pass
    
    @abstractmethod
    def mark_as_notimportant(self):
        pass

    @abstractmethod
    def add_to_myday(self):
        pass

    @abstractmethod
    def remove_from_myday(self):
        pass
