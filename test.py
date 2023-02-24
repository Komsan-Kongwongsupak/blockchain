from Blockchain import BlockChain
from Block import Block

'''
Create, display, and validate the block.
'''
print('\n########## BLOCK ZONE ##########\n')
a = Block(0, ['abc', 'def'])

print('\nORIGINAL BLOCK')
a.display()
print()

# a.set_hash_prev(123)
# a.display()
# print()
# a.mine()
# a.display()
# print()

# new_nonce = 123
# a.set_nonce(new_nonce)
# print(f'The nonce is modified from {a.get_nonce()} to {new_nonce}!')
# a.display()
# print()
# a.mine()
# a.display()
# print()

# a.set_transactions(['ace', 'zyx'])
# a.display()
# print()
# a.mine()
# a.display()
# print()

'''
Create, display, and validate the blockchain.
'''
print('########## BLOCKCHAIN ZONE ##########\n')
xyz = BlockChain()
print()
xyz.append_block(['abc', 'def'])
print()
xyz.append_block(['ghi', 'jkl'])
print()
xyz.append_block(['mno', 'pqr'])
print()
xyz.append_block(['stu', 'vwx'])

print('\nORIGINAL BLOCKCHAIN')
xyz.display()
print()

# xyz.delete_block(1)
# print()
# xyz.display()
# print()

# xyz.data[2].set_transactions(['ace', 'zyx'])
# print()
# xyz.display()
# print()
# xyz.data[2].mine()
# print()
# xyz.display()
# print()