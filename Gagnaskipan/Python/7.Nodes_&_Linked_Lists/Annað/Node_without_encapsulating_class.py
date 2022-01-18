
class Node():
    def __init__(self, data=None, next=None):
        self.data = data    # 7
        self.next = next    # None


def push_front(head, data):
    node = Node(data, head)
    return node

def print_content(head):
        current_node = head
        while current_node != None:
                print(current_node)
                current_node = current_node.next

#    if head.next != None:
#        print(head.data)
#        print_content(head.next)

def remove_front(head):
    while head.next != None:
        head = head.next    

def push_back(head, data):
    current_node = Node(data, None)
    if head.next != None:
        head = head.next
    head.next = current_node


head = Node()
head = push_front(head, 7)
head = push_front(head, 34)
head = push_front(head, 525)
head = push_front(head, 290)
head = push_front(head, 94)
print_content(head)
print("-------------------")

remove_front(head)
print_content(head)
print("-------------------")

push_back(head, 101)
# print_content(head)