from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
import rc4
node = Flask(__name__)

# Define what a Snakecoin block is
class Block:
  def __init__(self, index, transactionId, timestamp, proof_of_work, encryptActCode, previous_hash):
    self.index = index
    self.transactionId = transactionId
    self.timestamp = timestamp
    self.proof_of_work = proof_of_work
    self.encryptActCode = encryptActCode
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
#calculating the hash from previous hash 
  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + str(self.timestamp) + str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()
  
# Generate genesis block
def create_genesis_block():
  # Manually construct a block with index zero and 0 previous hash
  return Block(0, -1, date.datetime.now(), 9, "init", "0") # TransactioId for block 1 is -1, activation code is init


# # A completely random address of the owner of this node
# miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
# This node's blockchain copy
blockchain = []
blockchain.append(create_genesis_block())
# Store the transactions that this node has in a list
# this_nodes_transactions = []
# Store the url data of every other node in the network so that we can communicate with them
# peer_nodes = []
# # A variable to deciding if we're mining or not
# mining = True

@node.route('/txion', methods=['POST'])                     #????????????
def transaction():
  # On each new POST request, we extract the transaction data     
  # new_txion = request.get_json() 
  
  # Call mine with some encrypted activation code
  prodID = request.prodID # FIGURE OUT HOW DATA IS COMING
  sha = hasher.sha256()
  sha.update((str(prodID) + str(date.datetime.now())).encode('utf-8'))
  actCode = "".join(sha.hexdigest()[::4])
  key = generateKey()
  encryptActCode = encrypt(actCode, key)
  mine(encryptActCode) 

  return "Transaction added on blockchain successfully\n"   #????????????

def generateKey():    #needs to be done
  generated = "key"
  return generated

def encrypt(plain_text, key): # assuming key and plain_text are equal in length
  encrypted = ""
  for pt, k in zip(plain_text, key):
    encrypted += format((ord(pt) ^ ord(k)), "02X")
  return encrypted

# @node.route('/blocks', methods=['GET'])
# def get_blocks():
#   chain_to_send = blockchain
#   # Convert our blocks into dictionaries so we can send them as json objects later
#   for i in range(len(chain_to_send)):
#     block = chain_to_send[i]
#     block_index = str(block.index)
#     block_timestamp = str(block.timestamp)
#     block_data = str(block.data)
#     block_hash = block.hash
#     chain_to_send[i] = {
#       "index": block_index,
#       "timestamp": block_timestamp,
#       "data": block_data,
#       "hash": block_hash
#     }
#   chain_to_send = json.dumps(chain_to_send)
#   return chain_to_send

# function to search blockchain
def search_blockchain(transactionId):
  existInChain = False
  for block in blockchain:
    if transactionId == block.transactionId:
        existInChain = True
        return block.encryptActCode

  if existInChain == False:
    print("Transaction doesn't exist\n")

# def find_new_chains():
#   # Get the blockchains of every other node
#   other_chains = []
#   for node_url in peer_nodes:
#     # Get their chains using a GET request
#     block = requests.get(node_url + "/blocks").content
#     # Convert the JSON object to a Python dictionary
#     block = json.loads(block)
#     # Add it to our list
#     other_chains.append(block)
#   return other_chains

# def consensus():
  # Get the blocks from other nodes
  other_chains = find_new_chains()
  # If our chain isn't longest, then we store the longest chain
  longest_chain = blockchain
  for chain in other_chains:
    if len(longest_chain) < len(chain):
      longest_chain = chain
  # If the longest chain isn't ours, then we stop mining and set our chain to the longest one
  blockchain = longest_chain

def get_proof_of_work(last_proof):
  # Create a variable that we will use to find our next POW
  incrementor = last_proof + 1
  #keep increasing incrementor till div by 9 and prev POW
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0) :
    incrementor += 1
  #return that as the POW
  return incrementor

@node.route('/mine', methods = ['GET'])
def mine(encryptActCode):
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof-of-work']
  # Find the POW for the current block being mined

  proof = get_proof_of_work(last_proof)

  new_block_index = last_block.index + 1
  new_block_transactionId = "Txn" + str(new_block_index)
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  
  mined_block = Block(
    new_block_index,
    new_block_transactionId,
    new_block_timestamp,
    proof,
    encryptActCode,
    last_block_hash
  )

  blockchain.append(mined_block)

# node.run()
