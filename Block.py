class Block:

    def __init__(self, hash_prev, transactions):
        self.hash_prev = hash_prev
        self.transactions = transactions
        self.hash_itself = self.generate_hash_itself()
        
    def get_hash_prev(self):
        return self.hash_prev
            
    def set_hash_prev(self, hash_prev):
        self.hash_prev = hash_prev
        self.hash_itself = self.generate_hash_itself()
        
    def get_transactions(self):
        return self.transactions
        
    def set_transactions(self, transactions):
        self.transactions = transactions
        self.hash_itself = self.generate_hash_itself()
        
    def reset_transactions(self):
        self.set_transactions([])
        
    def generate_hash_itself(self):
        return hash(str(self.get_hash_prev()) + ','.join(self.transactions))
        
    def get_hash_itself(self):
        return self.hash_itself