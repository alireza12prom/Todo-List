from abc import ABC, abstractproperty

class ITask(ABC):

    @abstractproperty
    def ID(self):
        pass
    
    @abstractproperty
    def title(self):
        pass
    
    @abstractproperty
    def description(self):
        pass
    
    @abstractproperty
    def date(self):
        pass

    @abstractproperty
    def state(self):
        pass

    @abstractproperty
    def important(self):
        pass
