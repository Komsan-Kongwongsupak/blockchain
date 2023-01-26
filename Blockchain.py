from Block import Block

class BlockChain:

    def __init__(self):
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
    
    def is_valid(self):
        data = self.get_data()
        if len(data) == 0:
            return True
        else:
            if data[0].get_hash_prev() != '0':
                return False
            else:
                for i in range(1, len(data)):
                    if data[i].get_hash_prev() != data[i - 1].get_hash_itself():
                        return False
                return True