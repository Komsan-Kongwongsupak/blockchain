from Block import Block

class BlockChain:

    def __init__(self):
        print('\nA new blockchain is created.')
        self.data = []
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def reset_data(self):
        self.set_data([])
    
    def add_block(self, transactions):
        hash_prev = '0' if len(self.data) == 0 else self.data[-1].get_hash_itself()
        self.data.append(Block(hash_prev, transactions))
    
    def pop_block(self):
        return self.data.pop()
    
    def display(self):
        print('----------------------------------')
        for one_block in self.get_data():
            one_block.display()
            print('----------------------------------')
        print(f'The blockchain is {"in" if not self.is_valid() else ""}valid.')
    
    def is_valid(self):
        for one_block in self.get_data():
            if not one_block.is_valid():
                return False
        return True
