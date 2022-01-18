from Node import Node

def print_linked_list(head):
    if (head != None):
        print(head.data)
        print_linked_list(head.next)
    #while head != None:
    #    print(head.data)
    #    head = head.next

def add_front(head = None, value = None):
    new_node = Node(value, head)
    return new_node

def add_end(head, value):
    end = getEnd(head)
    end.next = Node(value, None)

def remove_front(head):
    if head != None:
        return head.next

def remove_end(head):
    second_end = getSecondEnd(head)
    second_end.next = None

def getSecondEnd(head):
    while head.get_next().get_next() != None:
        head = head.next
    return head

def getEnd(head):
    while head.get_next() != None:
        head = head.next
    return head