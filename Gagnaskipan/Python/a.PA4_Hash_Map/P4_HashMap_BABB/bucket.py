
class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass


class Node():
    def __init__(self, key = 0, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next


class Bucket():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, value):
        """ Adds a value pair (key & data) to the collection.
            If equal key is already in the collection, raise ItemExistsException(). """
        if self.size == 0:
            new_node = Node(key, value, self.head)
            self.head = new_node
            self.size += 1  
        else:
            curr_key = self.head
            while curr_key != None:
                if curr_key.key == key:
                    raise ItemExistsException()
                else:
                    curr_key = curr_key.next

            new_node = Node(key, value, self.head)
            self.head = new_node
            self.size += 1

    def find(self, key):
        """ Returns the ​data​ value of the value pair with equal ​key.
            If equal key is not in the collection, raise NotFoundException(). """
        try:
            next_item = self.head
            while next_item.key != key:
                next_item = next_item.next
            else:
                return next_item.data
        except:
            raise NotFoundException()

    def update(self, key, value):
        """ Sets the data value of the value pair with equal ​key​ to ​data. 
            If equal key is not in the collection, raise NotFoundException(). """ 
        if self.size == 0:
            raise NotFoundException()
        else:  
            curr_key = self.head
            while curr_key != None:
                if curr_key.key != key:                
                    curr_key = curr_key.next
                elif curr_key.key == key:
                    curr_key.data = value
                    break
            if curr_key == None:
                raise NotFoundException()

    def contains(self, key):
        """ Returns ​True if equal ​key​ is found in the collection, otherwise ​False. """
        curr_key = self.head
        while curr_key != None:
            if curr_key.key == key:
                return True
            else:
                curr_key = curr_key.next
        return False

    def remove(self, key):
        """ Removes the value pair with equal ​key​ from the collection. 
            If equal key is not in the collection, raise NotFoundException(). """
        find_item = self.head

        if find_item.key == key:
            self.head = self.head.next
        else:
            while find_item.next != None:
                if find_item.next.key == key:
                    find_item.next = find_item.next.next
                    self.size -= 1
                    return None
                find_item = find_item.next
        self.size -= 1
        

    def __setitem__(self, key, data):
        """ Override to allow this syntax:  some_hash_map[key] = data 
            If equal ​key​ is already in the collection, update its ​data​ value.
            Otherwise add the value pair to the collection. """
        try:
            _ = self.find(key)
            _ = data
        except:
            self.insert(key, data)


    def __getitem__(self, key):
        """ Override to allow this syntax:  my_data = some_bucket[key] 
            Returns the ​data value of the value pair with equal ​key. 
            If equal key is not in the collection, raise NotFoundException(). """
        the_key = self.head
        while the_key != None:
            if the_key.key == key:
                return the_key.data
            the_key = the_key.next
        raise NotFoundException()


    def __len__(self):
        """ Override to allow this syntax:  length_of_structure = len(some_bucket) 
            Returns the number of items in the entire data structure. """ 
        return self.size


    def __str__(self):
        """ Collects all key-value that are in the 'Bucket' into a string, 
            where each key-value are seperated with a new line. """
        next_item = self.head
        ret_str = ""
        while next_item != None:
            ret_str += str(next_item.key) + " " + str(next_item.data) + "\n"
            next_item = next_item.next            
        return ret_str

