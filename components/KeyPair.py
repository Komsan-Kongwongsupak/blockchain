from .BasicComponent import BasicComponent
from ecdsa import SigningKey, VerifyingKey, BadSignatureError

class KeyPair(BasicComponent):

    __public_key: VerifyingKey
    __private_key: SigningKey

    def __init__(self):
        super().__init__()
        self.__private_key = SigningKey.generate()
        self.__public_key = self.__private_key.verifying_key
        self.validate()
    
    def get_public_key(self):
        return self.__public_key
    
    def set_public_key(self, public_key):
        self.__public_key = public_key
    
    def get_private_key(self):
        return self.__private_key
    
    def set_private_key(self, private_key):
        self.__private_key = private_key

    def __repr__(self):
        self.validate()
        return f'This key pair is {super().__repr__()}.\n' + f'Public Key: {self.__public_key.to_string().hex()}\n' + f'Private Key: {self.__private_key.to_string().hex()}'

    def validate(self):
        __test_str = b'test'
        __sim_signature = self.__private_key.sign(__test_str)
        try:
            if self.__public_key.verify(__sim_signature, __test_str):
                self.set_valid(True)
        except BadSignatureError:
            self.set_valid(False)
    
    def is_valid(self):
        self.validate()
        return super().is_valid()