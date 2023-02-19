class Block:

    def __init__(self, hash_prev, transactions):
        print('\nA new block is created.')
        self.hash_prev = hash_prev
        self.nonce = 0
        self.transactions = transactions
        self.hash_itself = self.generate_hash_itself()
        self.mine()
        
    def get_hash_prev(self):
        return self.hash_prev
            
    # for security testing only
    def set_hash_prev(self, hash_prev):
        hash_prev_prev = self.hash_prev
        self.hash_prev = hash_prev
        self.hash_itself = self.generate_hash_itself()
        print(f'\nThe previous hash is modified from {hash_prev_prev} to {self.hash_prev}!\n')
    
    def get_nonce(self):
        return self.nonce
    
    def set_nonce(self, nonce):
        self.nonce = nonce
        self.hash_itself = self.generate_hash_itself()
        
    def get_transactions(self):
        return self.transactions
        
    # for security testing only
    def set_transactions(self, transactions):
        transactions_prev = self.transactions
        self.transactions = transactions
        self.hash_itself = self.generate_hash_itself()
        print(f'\nThe transactions are modified from {transactions_prev} to {self.transactions}!\n')
        
    def generate_hash_itself(self):
        return abs(hash(str(self.get_hash_prev()) + str(self.get_nonce()) + ','.join(self.transactions)))
        
    def get_hash_itself(self):
        return self.hash_itself
    
    def display(self):
        print(f'previous hash: {self.get_hash_prev()}')
        print(f'nonce: {self.get_nonce()}')
        print(f'transactions: {self.get_transactions()}')
        print(f'current hash: {self.get_hash_itself()}')
        print(f'This block is {"in" if not self.is_valid() else ""}valid.')
    
    def is_valid(self):
        return str(self.get_hash_itself())[:4] == '1111'
    
    def mine(self):
        nonce = self.get_nonce()
        while not self.is_valid():
            nonce += 1
            self.set_nonce(nonce)
        print('This block is mined.')
