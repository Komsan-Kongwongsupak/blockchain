class BasicComponent:

    __valid: bool

    def __repr__(self):
        return f'{"" if self.__valid else "in"}valid'

    def validate(self):
        pass

    def is_valid(self):
        return self.__valid
    
    def set_valid(self, valid):
        self.__valid = valid