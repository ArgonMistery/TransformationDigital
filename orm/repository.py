from abc import ABC,abstractmethod
from sqlalchemy import text

class Abstract_Repository(ABC):
    
    @abstractmethod
    def add(self,model_type:object):
        raise NotImplementedError

    @abstractmethod
    def get(self,model_type:object):
        raise NotImplementedError

class RepositoryOne(Abstract_Repository):

    def __init__(self,session)->None:
        self.session=session

    def add(self, model_type):
        self.session.add(model_type)
        self.session.commit()
    
    def get(self, model_type):
        return self.session.query(model_type).all()
    