class DoubleLinkedList():
    class Node():
        def __init__(self, data=None, prev=None, next_=None):
            self._data = data
            self._prev = prev
            self._next = next_
    def __init__(self):
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    # Add between two nodes
    def add_between(self, new_node):
        new_node._prev._next = new_node
        new_node._next._prev = new_node
        self._size += 1
    
    # Remove between two nodes
    def remove_between(self, prev_node, next_node):
        if self.isEmpty() == False:
            prev_node._next = next_node
            next_node._prev = prev_node
            self._size -= 1
    
    # Check if empty
    def isEmpty(self):
        return self._size == 0
    
    # Gets the size of the list
    def getSize(self):
        return self._size
    
    # Print Frontwards
    def print_front(self,):
        curr = self._header._next
        ret_str = ""
        while curr._next != None:
            ret_str += str(curr._data) + " "
            curr = curr._next
        print(ret_str)
    
    # Print Backwards
    def print_back(self):
        curr = self._trailer._prev
        ret_str = ""
        while curr._prev != None:
            ret_str += str(curr._data) + " "
            curr = curr._prev
        print(ret_str)

class DLL_Deque(DoubleLinkedList):
    
    def __init__(self):
        super().__init__()
    
    # Get First and Last
    def first(self):
        return self._header._next._data
    def last(self):
        return self._trailer._prev._data
    
    # Add node First or Last
    def add_first(self, value):
        new_node = self.Node(value, self._header, self._header._next)
        self.add_between(new_node)
    def add_last(self, value):
        new_node = self.Node(value, self._trailer._prev, self._trailer)
        self.add_between(new_node)
    
    # Remove first or last node
    def remove_first(self):
        self.remove_between(self._header, self._header._next._next)
    def remove_last(self):
        self.remove_between(self._trailer._prev._prev, self._trailer)

class DLL_PosList(DoubleLinkedList):    
    def __init__(self):
        super().__init__()
        self._current_node = self._trailer
        self._current_position = 0
    
    def insert(self, value):
        new_node = self.Node(value, self._current_node._prev, self._current_node)
        self.add_between(new_node)
        self._current_node = new_node

    def move_to_next(self):
        if self._current_node._next != None:
            self._current_node = self._current_node._next
    def move_to_prev(self):
        if self._current_node._prev != None:
            self._current_node = self._current_node._prev

    def get_value(self):
        return self._current_node._data
    
    def remove(self):
        self.remove_between(self._current_node._prev, self._current_node._next)
        if self.isEmpty() == False:
            if self._current_node._next._next == None:
                self._current_node = self._current_node._prev
            else:
                self._current_node = self._current_node._next

# DOUBLE LINKED POSITIONAL LIST   
#doubleLinked = DLL_PosList()
#
#doubleLinked.insert(1)
#doubleLinked.insert(2)
#doubleLinked.insert(3)
#
#doubleLinked.move_to_next()
#doubleLinked.move_to_prev()
#
#print(doubleLinked.get_value())
#
#doubleLinked.print_front()
#print(doubleLinked.getSize())
#doubleLinked.remove()
#
#doubleLinked.print_front()
#print(doubleLinked.getSize())
#doubleLinked.remove()
#print(doubleLinked.getSize())
#doubleLinked.print_front()
#doubleLinked.print_back()
#
#
# DEQUE
#deque = DLL_Deque()
#
#deque.add_first(1)
#
#deque.add_last(4)
#
#deque.remove_first()
#deque.remove_last()
#
#deque.print_front()
#deque.print_back()