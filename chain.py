from hashlib import sha256
import json, time


class Block():
  def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
    self.index = index
    self.transactions = transactions
    self.timestamp = timestamp
    self.previous_hash = previous_hash
    self.nonce = nonce
    
  def computeHash(self):
    block_string = json.dumps(self.__dict__, sort_keys=True)
    return sha256(block_string.encode()).hexdigest()


class BlockChain():
  def __init__(self):
    self.chain = []
    self.transaction_pool = []
    
    self.difficulty = 1
    
    self.createFistBlock()
  
  def createFistBlock(self):
    genesis_block = Block(0, [], time.time(), "0")
    genesis_block.hash = genesis_block.compute_hash()
    print("First Block Hash: ", genesis_block.hash)
    self.chain.append(genesis_block)
    
  @property
  def lastBlock(self):
    return self.chain[-1]

  def proofOfWork(self, block):
    block.nonce += 1
    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * self.difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash()
    return computed_hash
  
  