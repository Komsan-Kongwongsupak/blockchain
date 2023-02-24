from Block import Block

class BlockChain:

    def __init__(self):
        print('A new blockchain is created.')
        self.data = []
        self.valid = True
        self.validate()
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        self.valid = False
        print(f'The whole data is modified!')
    
    def append_block(self, transactions):
        hash_prev = '0' if len(self.get_data()) == 0 else self.data[-1].get_hash_itself()
        self.data.append(Block(hash_prev, transactions))
        self.validate()
        print(f'The block is appended to the blockchain.')
    
    def delete_block(self, index):
        del self.data[index]
        self.validate()
        print(f'Block #{index} is deleted from the blockchain!')
    
    def display(self):
        print('----------------------------------')
        for one_block in self.get_data():
            one_block.display()
            print('----------------------------------')
        self.validate()
        print(f'The blockchain is {"in" if not self.is_valid() else ""}valid.')
    
    def is_valid(self):
        return self.valid
    
    def validate(self):
        chain = self.get_data()
        for i in range(len(chain)):
            if not chain[i].is_valid() or ((i > 0) and (chain[i].get_hash_prev() != chain[i - 1].get_hash_itself())):
                self.valid = False
                break