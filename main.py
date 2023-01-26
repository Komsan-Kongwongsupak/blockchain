from Blockchain import BlockChain

bc = BlockChain()
bc.add_block(['A transfers $10 to B', 'A transfers $5 to C'])
bc.add_block(['B transfers $20 to D'])
bc_data = bc.get_data()
print('.\n'.join([(', and ').join(bc_data[i].get_transactions()) for i in range(len(bc_data))]) + '.')
print(f"The blockchain is {'' if bc.is_valid() else 'in'}valid.")
