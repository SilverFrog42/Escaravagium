import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        b = bytes((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)), 'utf-8')
        m = hashlib.sha256(b)
        m = m.hexdigest()
        return m