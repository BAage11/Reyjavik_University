from Node import Node
from NodeMethods import *

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1
    
    def pop(self):
        temp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return temp
    
    def __str__(self):
        string = self.getString(self.head)
        return string
    
    def getString(self, head):
        if(head.next != None):
            return "{} {}".format(head.data, self.getString(head.next))
        return "{}".format(head.data)


        

queue = Queue()
queue.push(15)
queue.push(12)
queue.push(13)
queue.push(14)
print(queue.pop())
print(queue)


##############################################################

class NewItem():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Queue2():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        if self.head == None:
            self.head =  NewItem(value)
        elif self.tail == None:
            self.tail = NewItem(value, None, self.head)
            self.head.next = self.tail
        else:
            new_item = NewItem(value, None, self.tail)
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1

    def remove(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        curr_node = self.head
        ret_str = ""
        while curr_node != None:
            ret_str += str(curr_node.value) + " "
            curr_node = curr_node.next
        return ret_str


print("\nNew queue:")
queue2 = Queue2()
queue2.add(10)
queue2.add(12)
queue2.add(13)
queue2.add(15)
queue2.add(17)
queue2.add(19)
print(queue2)
print("size of queue:", len(queue2))
queue2.remove()
queue2.remove()
print(queue2)
print("size of queue:", len(queue2))
