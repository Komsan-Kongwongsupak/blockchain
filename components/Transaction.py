from .AdvancedComponent import AdvancedComponent
from datetime import datetime
from .KeyPair import KeyPair
from ecdsa import BadSignatureError

class Transaction(AdvancedComponent):

    __datetime: datetime
    __money: int
    __sender_id: str
    __receiver_id: str
    __data: bytes
    __key: KeyPair
    __signature: bytes

    def __init__(self, money, sender_id, receiver_id):
        super().__init__()
        self.__datetime = datetime.now()
        self.__money = money
        self.__sender_id = sender_id
        self.__receiver_id = receiver_id
        self.__data = (str(self.__datetime) + str(self.__money) + self.__sender_id + self.__receiver_id).encode()
        self.__key = KeyPair()
        self.__signature = self.__key.get_private_key().sign(self.__data)
        self.validate()
    
    def get_money(self):
        return self.__money
    
    def set_money(self, money):
        self.__money = money
    
    def get_sender_id(self):
        return self.__sender_id
    
    def set_sender_id(self, sender_id):
        self.__sender_id = sender_id
    
    def get_receiver_id(self):
        return self.__receiver_id
    
    def set_receiver_id(self, receiver_id):
        self.__receiver_id = receiver_id
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def get_key(self):
        return self.__key
    
    def set_key(self, key):
        self.__key = key
    
    def get_signature(self):
        return self.__signature
    
    def set_signature(self, signature):
        self.__signature = signature
    
    def __repr__(self):
        self.validate()
        adv_comp_by_part = super().__repr__().split('\n')
        return adv_comp_by_part[0] + f'\nThis transaction is {adv_comp_by_part[1]}.\n' + f'Date and Time: {self.__datetime}\n' + f'User {self.__sender_id} sends {self.__money} Unit to User {self.__receiver_id}.\n' + ('-' * 100) + '\n' + 'Key:\n' + self.__key.__repr__() + '\n' + ('-' * 100) + f'\nSignature: {self.__signature.hex()}'
    
    def validate(self):
        try:
            if (self.__money > 0) and (self.__key.is_valid()) and (self.__key.get_public_key().verify(self.__signature, self.__data)):
                self.set_valid(True)
            else:
                self.set_valid(False)
        except BadSignatureError:
            self.set_valid(False)
    
    def is_valid(self):
        self.validate()
        return super().is_valid()