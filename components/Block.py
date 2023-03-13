from .AdvancedComponent import AdvancedComponent

class Block(AdvancedComponent):

    __hash_previous: int
    __nonce: int
    __transactions: list
    __hash: int

    def __init__(self, hash_previous, transactions):
        super().__init__()
        self.__hash_previous = hash_previous
        self.__nonce = 0
        self.__transactions = transactions
        self.generate_hash()
        self.validate()
        self.mine()
        
    def get_hash_previous(self):
        return self.__hash_previous
    
    def set_hash_prev(self, hash_previous):
        self.__hash_previous = hash_previous
    
    def get_nonce(self):
        return self.__nonce
    
    def set_nonce(self, nonce):
        self.__nonce = nonce
        
    def get_transactions(self):
        return self.__transactions
    
    def set_transactions(self, transactions):
        self.transactions = transactions
        
    def generate_hash(self):
        self.__hash = abs(hash(str(self.__hash_previous) + str(self.__nonce) + ''.join([transac.get_data().decode() for transac in self.__transactions])))
        
    def get_hash(self):
        return self.__hash
    
    def set_hash(self, hash):
        self.__hash = hash
    
    def __repr__(self):
        self.validate()
        adv_comp_by_part = super().__repr__().split('\n')
        return adv_comp_by_part[0] + f'\nThis block is {adv_comp_by_part[1]}.\n' + f'Hash of the Previous Block: {self.__hash_previous}\n' + f'Nonce: {self.__nonce}\n' + ('*' * 100) + '\n' + (('*' * 100) + '\n').join(['Transaction:\n' + str(transac) + '\n' for transac in self.__transactions]) + ('*' * 100) + f'\nHash: {self.__hash}'
    
    def validate(self):
        self.set_valid(bool(str(self.__hash)[:4] == '1111'))
    
    def is_valid(self):
        self.validate()
        return super().is_valid()
    
    def mine(self):
        nonce = self.__nonce
        while not self.is_valid():
            nonce += 1
            self.set_nonce(nonce)
            self.generate_hash()
            self.validate()
        pass
