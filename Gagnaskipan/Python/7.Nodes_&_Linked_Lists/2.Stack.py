class Stack:
    class Node:
        # Init for 'Node'
        def __init__(self, value=None, next_node=None):
            self.value = value
            self.next_node = next_node
        
        # Property functions (getters and setters)
        def get_value(self):
            return self.value

        def get_next_node(self):
            return self.next_node
        
        def set_value(self, value):
            self.value = value
        
        def set_next_node(self, next_node):
            self.next_node = next_node
    

    # Init for 'Stack'
    def __init__(self):
        self.size = 0
        self.head = None
        self.current_node = self.head

    # Push to a new value to the front
    def push(self, value):
        new_node = self.Node(value, self.head)
        self.head = new_node
        self.current_node = self.head
        self.size += 1
    
    # Pop from the top and return the value
    def pop(self):
        if self.head == None:
            return
        return_value = self.head.get_value()
        self.head = self.head.get_next_node()
        self.current_node = self.head
        self.size -= 1
        return return_value
    
    # Returns the size of the stack
    def get_size(self):
        return self.size
    
    # Returns the stack in one line
    def __str__(self):
        str_builder = ""
        while self.current_node != None:
            str_builder += str(self.current_node.get_value()) + "\n"
            self.current_node = self.current_node.get_next_node()
        self.current_node = self.head
        return str_builder


s = Stack()

s.push("world")
s.push("hello")
s.push("test")
print()
print(s)
print("----------------")
print("Stack is currently with {} items.\n".format(s.get_size()))

s.pop()
s.pop()
print(s)
print("----------------")
print("Stack is currently with {} items.\n".format(s.get_size()))

s.push(4)
s.push(5)
s.push(10)
print(s)
print("----------------")
print("Stack is currently with {} items.\n".format(s.get_size()))

s.pop()
print(s)
print("----------------")
print("Stack is currently with {} items.\n".format(s.get_size()))