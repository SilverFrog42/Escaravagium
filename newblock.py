import time
import block
import userdata

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = time.time()
  this_data = userdata.input_data() + str(this_index)
  this_hash = last_block.hash
  return block.Block(this_index, this_timestamp, this_data, this_hash)