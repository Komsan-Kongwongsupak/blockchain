from .BasicComponent import BasicComponent
from uuid import uuid4

class AdvancedComponent(BasicComponent):

    # "id" is a class property that stores the ID number of the class object.
    __id: str = None

    def __init__(self):
        super().__init__()
        self.generate_id()

    def __repr__(self):
        return f'ID Number: {self.__id}\n' + super().__repr__()

    def generate_id(self):
        self.__id = str(uuid4())
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
