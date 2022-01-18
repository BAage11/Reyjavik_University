class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node



head = None
def push_front(head, value):
    new_node = Node(value, head)
    return new_node

def remove_front(head):
    if head == None:
        return
    return_node = head.get_next_node()
    del head
    return return_node

def push_back(head, data):
    if head.get_next_node() == None:
        new_node = Node(data)
        head.set_next_node(new_node)
    else:
        push_back(head.get_next_node(), data)
    return head

def remove_back(head):
    if head.get_next_node().get_next_node() == None:
        next_node = head.get_next_node()
        del next_node
        head.set_next_node(None)
    else:
        remove_back(head.get_next_node())
    return head

def print_iterative(head):
    while head != None:
        print(head.get_value())
        head = head.get_next_node()

def length_list(head):
    if head == None:
        return 0
    else:
        return 1 + length_list(head.next_node)


# VILLA Í LOK LISTANS !!
def insert_value(head, data):
    if head == None or head.value >= data:
        head = push_front(head, data)
        return head
        # eða 'return Node(data, head)'
    node = head
    previous = head
    while node.next_node != None and node.value < data:
        previous = node
        node = node.next_node
    previous.next_node = Node(data, node)
    return head    


# ÓKLÁRAÐ !!!
def reverse(head):
    node = head
    while node != None:
        while node.next_node != None:
            node = node.next_node
        node.next_node = None
    return head


print("\nPUSH FRONT:")
head = push_front(head, 6)
head = push_front(head, 5)
head = push_front(head, 4)
head = push_front(head, 3)
head = push_front(head, 2)
head = push_front(head, 1)
print_iterative(head)
print("---------------------")

print("\nREMOVE FRONT:")
head = remove_front(head)
head = remove_front(head)
head = remove_front(head)
print_iterative(head)
print("---------------------")

print("\nPUSH BACK:")
head = push_back(head, 10)
head = push_back(head, 12)
head = push_back(head, 14)
head = push_back(head, 16)
head = push_back(head, 18)
print_iterative(head)
print("---------------------")

print("\nREMOVE BACK:")
head = remove_back(head)
head = remove_back(head)
head = remove_back(head)
print_iterative(head)
print("---------------------")

print("LENGTH OF THE LIST:")
size = length_list(head)
print(size)

print("\nADD VALUE IN SORTED LIST:")
insert_value(head, 22)
insert_value(head, 7)
insert_value(head, 15)
print_iterative(head)
print("---------------------")

print("\nREVERSED LIST:")
head = reverse(head)
print_iterative(head)
print("---------------------")
