# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [[] for _ in range(capacity)]

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.s

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        hash_key = self._hash_mod(key)
        exists = False
        bucket = self.storage[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                exists = True
                break
        if exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        bucket = self.storage[hash_key]
        exists = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                exists = True
                break
        if exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        bucket = self.storage[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        temp_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [[] for _ in range(self.capacity)]

        for i in temp_storage:
            for j in i:
                self.insert(j[0], j[1])


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
