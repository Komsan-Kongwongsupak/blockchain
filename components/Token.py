from .AdvancedComponent import AdvancedComponent
from .Blockchain import Blockchain

class Token(AdvancedComponent):

    __nodes: list

    def __init__(self, number_of_nodes):
        super().__init__()
        self.__nodes = [Blockchain()] * number_of_nodes
        self.validate()
    
    def get_nodes(self):
        return self.__nodes
    
    def set_nodes(self, nodes):
        self.__nodes = nodes
    
    def update_nodes(self, transactions):
        for node in self.__nodes:
            node.append_new_block(transactions)
    
    def __repr__(self):
        self.validate()
        adv_comp_by_part = super().__repr__().split('\n')
        return adv_comp_by_part[0] + f'\nThis token is {adv_comp_by_part[1]}.\n' + ('+' * 100) + '\n' + (('+' * 100) + '\n').join(['Node:\n' + str(node) + '\n' for node in self.__nodes]) + ('+' * 100)
    
    def validate(self):
        self.set_valid(len(set(self.__nodes)) == 1)
    
    def is_valid(self):
        self.validate()
        return super().is_valid()