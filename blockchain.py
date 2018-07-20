import genesis
import newblock

# Create the blockchain and add the genesis block
blockchain = [genesis.create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 100000000000000000000000000000000

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = newblock.next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print ("Hash: {}\n".format(block_to_add.hash))