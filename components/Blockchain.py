from .AdvancedComponent import AdvancedComponent
from .Block import Block

class Blockchain(AdvancedComponent):

    __chain: list

    def __init__(self):
        super().__init__()
        self.__chain = []
        self.validate()
    
    def get_chain(self):
        return self.__chain
    
    def set_chain(self, chain):
        self.__chain = chain
    
    def append_new_block(self, transactions):
        hash_previous = 0 if len(self.__chain) == 0 else self.__chain[-1].get_hash()
        self.__chain.append(Block(hash_previous, transactions))
    
    def __repr__(self):
        self.validate()
        adv_comp_by_part = super().__repr__().split('\n')
        return adv_comp_by_part[0] + f'\nThis blockchain is {adv_comp_by_part[1]}.\n' + ('#' * 100) + '\n' + (('#' * 100) + '\n').join(['Block:\n' + str(bl) + '\n' for bl in self.__chain]) + ('#' * 100)
    
    def validate(self):
        for bl in self.__chain:
            if not bl.is_valid():
                self.set_valid(False)
                return
        self.set_valid(True)
    
    def is_valid(self):
        self.validate()
        return super().is_valid()