from Blockchain import BlockChain
from Block import Block

'''
Create, display, and validate the block.
'''
# a = Block(0, ['abc', 'def'])

# print('\nORIGINAL BLOCK')
# a.display()

# a.set_hash_prev(123)
# a.display()
# a.mine()
# a.display()

# new_nonce = 123
# print(f'The nonce is modified from {a.get_nonce()} to {new_nonce}!')
# a.set_nonce(new_nonce)
# a.display()
# a.mine()
# a.display()

# a.set_transactions(['ace', 'zyx'])
# a.display()
# a.mine()
# a.display()

'''
Create, display, and validate the blockchain.
'''
xyz = BlockChain()
xyz.add_block(['abc', 'def'])
xyz.add_block(['ghi', 'jkl'])

print('\nORIGINAL BLOCKCHAIN')
xyz.display()
print()
