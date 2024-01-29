from hashlib import sha256
import json
from datetime import datetime


'''
Fixed parameters for transactions: type, bname, bphone, commodity, variety, date
Variable parameters : can go into a database with different tables for specific types.
'''

class Block:
    def __init__(self, index, previous_hash, details, timestamp, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.details = details
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()
        
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash
    
    def __str__(self):
        return str(self.__dict__)


class Blockchain:
    def __init__(self):
        self.hashes = []
        self.transactions = {}
        self.usertype_transactions = {
            'harvesting': [],
            'cooling': [], 
            'packing': [], 
            'shipping': [], 
            'receiving': []
        }
        self.genesis_block()

    def __str__(self):
        return str(self.__dict__)
    
    def genesis_block(self):
        genesis_block = Block('Genesis', 0x0, [3,4,5,6,7], f'{datetime.now().timestamp()}', 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.hashes.append(genesis_block.hash)
        # self.transactions.append(str(genesis_block.__dict__))
        self.transactions[genesis_block.hash] = genesis_block.__dict__
        return genesis_block
    
    def getLastBlock(self):
        return self.hashes[-1]

    def proof_of_work(self, block):
        difficulty = 1
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not (computed_hash.endswith('0' * difficulty) and ('55' * difficulty) in computed_hash):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add(self, data):
        block = Block(len(self.hashes), self.hashes[-1], data, f'{datetime.now().timestamp()}', 0)
        block.hash = self.proof_of_work(block)
        self.hashes.append(block.hash)
        # self.transactions.append(block.__dict__)
        self.transactions[block.hash] = block.__dict__
        self.usertype_transactions[data["type"]].append(block.__dict__)
        return json.loads(str(block.__dict__).replace('\'', '\"'))
    
    def getTransactions(self, id):
        # labels = ['Manufacturer', 'Transporter', 'Retailer']
        # labels = ['Harvesting','Cooling','Packing','Shipping','Receiving']
        while True:
            try: 
                if(id=='all'):
                    # print(self.usertype_transactions)
                    # print(self.transactions)
                    return self.transactions
                    # for i in range(len(self.transactions)-1):
                    #     transaction = self.transactions[i+1]
                    #     print(f'{transaction["details"]["type"]}:{i}\n{transaction}')
                    break
                else:
                    print(self.transactions[id])
                    break
            except Exception as e:
                print(e)