
class Node():
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, value): 
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop_front(self):
        current_node = self.head
        if current_node != None:
            self.head = current_node.next
            self.size -= 1
            return current_node.data
            
    def get_size(self):
        return self.size
    
    def __str__(self):
        ret_str = ""
        current_node = self.head
        while current_node != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next
        return ret_str

