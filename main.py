from Blockchain import BlockChain

bc = BlockChain()
bc.add_block(['A transfers $10 to B', 'A transfers $5 to C'])
bc.add_block(['B transfers $20 to D'])
bc.add_block(['C transfers $10 to A'])
bc_data = bc.get_data()
# print('.\n'.join([(', and ').join(bc_data[i].get_transactions()) for i in range(len(bc_data))]) + '.')
print(f'hash before = {bc_data[1].get_hash_itself()}')
bc_data[1].set_transactions(['D transfers $20 to B'])
print(f'hash after = {bc_data[1].get_hash_itself()}')
validity = bc.is_valid()