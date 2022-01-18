class Empty(Exception):
    pass

class DoubleLinkedList():
    class Node():
        def __init__(self, data = None, prev= None, _next = None):
            self.data = data
            self.prev = prev
            self._next = _next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header._next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        self.current_node = self.trailer

    def add_to_set(self, data):
        if self.is_empty():
            raise Empty("Collection is empty")
        value = self.header._next
        while value.data != None:
            if value.data == data:
                return
            value = value._next
        self.insert(data)

    def find(self, data):
        value = self.header._next()
        while value.data != None:
            if value.data == data:
                return True
            value = value._next
        return False

    def delete_set_item(self, data):
        pass

    def insert(self, data):
        new_pos = self.Node(data, self.current_node.prev, self.current_node)
        self.current_node = new_pos
        self.current_node.prev._next = new_pos
        self.current_node._next.prev = new_pos
        self.size += 1

    def get_size(self):
        return self.size

    def move_to_next(self):
        if self.is_empty():
            raise Empty("Collection is empty")
        else:
            self.current_node.data, self.current_node._next.data = self.current_node._next.data, self.current_node.data
        self.current_node = self.current_node._next
            
    def move_to_prev(self):
        if self.is_empty():
            raise Empty("Collection is empty")
        else:
            self.current_node.data, self.current_node.prev.data = self.current_node.prev.data, self.current_node.data
        self.current_node = self.current_node.prev

    def get_value(self):
        return self.current_node.data
    
    def is_empty(self):
        return self.size == 0

    def get_first(self):
        if self.is_empty():
            raise Empty("Collection is empty")
        return self.header._next.data

    def get_last(self):
        if self.is_empty():
            raise Empty("Collection is empty")
        return self.trailer.prev.data

    def insert_between(self, data, before, after):
        # Item before 'new_item' == 'before'
        # item after 'new item' == 'after'
        new_item = self.Node(data, before, after)
        before._next = new_item
        after.prev = new_item
        self.size += 1
        return new_item

    def add_first(self, data):
        self.insert_between(data, self.header, self.header._next)

    def add_last(self, data):
        self.insert_between(data, self.trailer.prev, self.trailer)

    def delete_node(self, data):
        before = data.prev      # Ná í gildið sem kemur eftir 'data'
        after = data._next       # Ná í gildið sem kemur á undan 'data'
        before._next = after     # Breyta gildi á eftir 'before' í 'after'
        after.prev = before     # Breyta gildi á undan 'after' í 'before'
        # Þar með er gildið 'data' ekki lengur með tengsl við listann
        self.size -= 1
        
    def remove(self):
        if self.current_node == None:
            raise Empty("Collection is empty")
        else:
            self.delete_node(self.current_node)
            self.current_node = self.current_node._next

    def remove_first(self):
        if self.header._next == None:
            raise Empty("Collection is empty")
        else:
            self.delete_node(self.header._next)

    def remove_last(self):
        if self.header._next == None:
            raise Empty("Collection is empty")
        else:
            self.delete_node(self.trailer.prev)

    def print_forward(self):
        current_node = self.header._next
        ret_str = ""
        while current_node.data != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node._next
        return ret_str

    def print_backward(self):
        current_node = self.trailer.prev
        ret_str = ""
        while current_node.data != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node.prev
        return ret_str

    def __str__(self):
        string_forward = self.print_forward()
        string_backwards = self.print_backward()
        return "String forward:  {}\nString backwards:  {}".format(string_forward, string_backwards)


poslist = DoubleLinkedList()
print("\nEmpty list:")
print(poslist)

poslist.add_first(11)
poslist.add_first(22)
poslist.add_first(33)
print("\nAdd first:")
print(poslist)

poslist.add_last(44)
poslist.add_last(55)
poslist.add_last(66)
print("\nAdd last:")
print(poslist)

first_item = poslist.get_first()
print("\nGet first:")
print(first_item)

last_item = poslist.get_last()
print("\nGet last:")
print(last_item)

poslist.remove_first()
print("\nRemove first:")
print(poslist)

poslist.remove_last()
print("\nRemove last:")
print(poslist)

poslist.insert(999)
poslist.insert(888)
print("\nInsert(at current node):")
print(poslist)

print("\nGet size:")
size = poslist.get_size()
print(size)

print("\nGet current node value:")
current_node = poslist.get_value()
print(current_node)

poslist.move_to_next()
print("\nMove current node further back:")
print(poslist)

print("\nGet current node value:")
current_node = poslist.get_value()
print(current_node)

poslist.move_to_prev()
print("\nMove current node further forward:")
print(poslist)

print("\nGet current node value:")
current_node = poslist.get_value()
print(current_node)

print("\nRemove (and change) current node from list:")
poslist.remove()
print(poslist)

print("\nGet current node value:")
current_node = poslist.get_value()
print(current_node)

print("\nFinished!!!\n")