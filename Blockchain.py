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
            print('The blockchain is valid.')
            return True
        else:
            if data[0].get_hash_prev() != '0':
                print(f'The genesis block is invalid.')
                print('------------------------------')
                data[0].display()
                print('------------------------------')
                return False
            else:
                for i in range(1, len(data)):
                    if data[i].get_hash_prev() != data[i - 1].get_hash_itself():
                        print(f'The intermediate block is invalid.')
                        print('------------------------------')
                        data[i - 1].display()
                        print('------------------------------')
                        data[i].display()
                        print('------------------------------')
                        if i + 1 < len(data):
                            data[i + 1].display()
                            print('------------------------------')
                        return False
                print('The blockchain is valid.')
                return True