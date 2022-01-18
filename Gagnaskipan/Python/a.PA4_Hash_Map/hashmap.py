from bucket import Bucket, ItemExistsException, NotFoundException

class HashMap():
    def __init__(self):
        self.list_size = 5
        self.hash_map = [Bucket() for _ in range(self.list_size)]
        self.count = 0
        

    def insert(self, key, data):
        """ Adds this value pair to the collection. 
            If equal key is already in the collection, raise ItemExistsException(). """
        if self.count >= (self.list_size * 1.2):
            self.rebuild()        
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        bucket.insert(key, data)
        self.count += 1


    def update(self, key, data):
        """ Sets the data value of the value pair with equal ​key to ​data. 
            If equal key is not in the collection, raise NotFoundException(). """
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        bucket.update(key, data)


    def find(self, key):
        """ Returns the ​data​ value of the value pair with equal ​key.
            If equal key is not in the collection, raise NotFoundException(). """
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        return bucket.find(key)


    def contains(self, key):
        """ Returns ​True​ if equal ​key​ is found in the collection, otherwise ​False. """ 
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        return bucket.contains(key)


    def remove(self, key):
        """ Removes the value pair with equal ​key from the collection. 
            If equal key is not in the collection, raise NotFoundException(). """ 
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        bucket.remove(key)
        self.count -= 1


    def __setitem__(self, key, data):
        """ Override to allow this syntax:  some_hash_map[key] = data 
            If equal ​key​ is already in the collection, update its ​data​ value. 
            Otherwise add the value pair to the collection. """
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        if bucket.contains:
            bucket[key] = data
        else:
            bucket.insert(key, data)
            self.count += 1

    def __getitem__(self, key):
        """ Override to allow this syntax:  my_data = some_hash_map[key] 
            Returns the ​data​ value of the value pair with equal ​key. 
            If equal key is not in the collection,​ raise NotFoundException(). """
        index = hash(key) % self.list_size
        bucket = self.hash_map[index]
        return bucket[key]

        
    def __len__(self):
        """ Override to allow this syntax:  length_of_structure = len(some_hash_map).
            Returns the number of items in the entire data structure. """
        size = 0
        for i in self.hash_map:
            size += len(i)
        return size


    def rebuild(self):
        """ When the number of items in the HashMap has reached 120% of the number of buckets (length of array or list) it must ​rebuild(), doubling the number of buckets. """
        self.list_size *= 2
        larger_hashmap = [Bucket() for _ in range(self.list_size)]
        for bucket in self.hash_map:
            curr_bucket = bucket.head
            while curr_bucket != None:
                index = hash(curr_bucket.key) % self.list_size
                larger_hashmap[index].insert(curr_bucket.key, curr_bucket.data)
                curr_bucket = curr_bucket.next
        self.hash_map = larger_hashmap


