from Node import Node
from NodeMethods import *

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_size(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop(self):
        temp = self.tail.data
        self.tail = getSecondEnd(self.head)
        self.tail.next = None
        self.size -= 1
        return temp

    def getSecondEnd(self, head):
        if (head.get_next() == None):
            return None
        while head.get_next().get_next() != None:
            head = head.next
        return head
    
    def __str__(self):
        string = self.getString(self.head)
        return string
    
    def getString(self, head):
        if (head.next != None):
            return "{} {}".format(head.data, self.getString(head.next))
        return "{}".format(head.data)


stack = Stack()
stack.push(15)
stack.push(19)
stack.push(11)
stack.push(12)
stack.push(13)
print(stack.get_size())
print(stack)
print()
print(stack.pop(), end=" end\n")
print(stack.pop(), end=" end\n")
print(stack.pop(), end=" end\n")
print(stack.pop(), end=" end\n")
print(stack.get_size())

print_linked_list(stack.head)
print(stack)


#################################################################

class NewItem():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack2():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        if self.head == None:
            self.head = self.tail = NewItem(value)
        else:
            new_item = NewItem(value)
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1

    def remove(self):
        if self.head == None:
            return
        else:
            curr_item = self.head
            while curr_item.next.next != None: 
                curr_item = curr_item.next
            if curr_item.next.next == None:
                curr_item.next = None
                self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        curr_item = self.head
        while curr_item != None:
            ret_str += str(curr_item.value) + " "
            curr_item = curr_item.next
        return ret_str


print("\nNew Stack:")
stack2 = Stack2()
stack2.add(5)
stack2.add(9)
stack2.add(1)
stack2.add(8)
stack2.add(3)
stack2.add(6)
print(stack2)
print("size of stack:", len(stack2))
stack2.remove()
print(stack2)
print("size of stack:", len(stack2))
