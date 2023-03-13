from .AdvancedComponent import AdvancedComponent
from .KeyPair import KeyPair

class User(AdvancedComponent):

    __firstname: str
    __middlename: str
    __lastname: str
    __full_name: str
    __key: KeyPair

    def __init__(self, firstname, middlename, lastname):
        super().__init__()
        self.__firstname = firstname
        self.__middlename = middlename
        self.__lastname = lastname
        self.generate_full_name()
    
    def get_firstname(self):
        return self.__firstname
    
    def set_firstname(self, firstname):
        self.__firstname = firstname
    
    def get_middlename(self):
        return self.__middlename
    
    def set_middlename(self, middlename):
        self.__middlename = middlename
    
    def get_lastname(self):
        return self.__lastname
    
    def set_lastname(self, lastname):
        self.__lastname = lastname
    
    def generate_full_name(self):
        full_name = [self.__firstname, self.__lastname]
        if self.__middlename != '':
            full_name.insert(1, self.__middlename)
        self.__full_name = ' '.join(full_name)
    
    def get_full_name(self):
        return self.__full_name
    
    def set_full_name(self, full_name):
        self.__full_name = full_name
    
    def generate_key(self):
        self.__key = KeyPair()
    
    def get_key(self):
        return self.__key
    
    def set_key(self, key):
        self.__key = key
    
    def __repr__(self):
        self.validate()
        return f'This user is {super().__repr__()}.\n' + f'Full Name: {self.__full_name}\n' + ('-' * 100) + '\n' + 'Key:\n' + self.__key.__repr__() + '\n' + ('-' * 100)
    
    def validate(self):
        self.set_valid(self.__key.is_valid())
    
    def is_valid(self):
        self.validate()
        return super().is_valid()