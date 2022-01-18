from Node import Node

# Verkefnatími 1 -------------------------------------------------------------------
def print_list(head):
    string = getString(head)
    print(string)
    
def getString(head):
    if(head.next != None):
        return "{} {}".format(head.data, getString(head.next))
    return "{}".format(head.data)

def add_front(head = None, value = None):
    new_node = Node(value, head)
    return new_node

def add_end(head, value):
    end = getEnd(head)
    if end == None:
        return Node(value, None)
    end.next = Node(value, None)
    return head


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

# Verkefnatími 2 -------------------------------------------------------------------
# Print
def lenght_recursive(head):
    if(head == None):
        return 0
    return 1 + lenght_recursive(head.next)

def lenght_iteratively(head):
    lenght = 0
    if(head == None):
        return lenght
    while head != None:
        lenght += 1
        head = head.next
    return lenght

# Sum
def sum_recursive(head):
    if(head == None):
        return 0
    return head.data + sum_recursive(head.next)

def sum_iteratively(head):
    summ = 0
    if(head == None):
        return summ
    while head != None:
        summ += head.data
        head = head.next
    return summ

# add in order
def add_ordered(head, value):
    if head == None or head.data > value:
        return Node(value, head)
    current_node = head
    while current_node.next != None and current_node.data < value:
        #print(current_node.data, "<=", value ,"<", current_node.get_next().data, current_node.data <= value < current_node.get_next().data)
        if current_node.data <= value < current_node.get_next().data: # note.next != None and note.data < value
            new_node = Node(value, current_node.get_next())
            current_node.next = new_node
            return head
        current_node = current_node.next
    current_node.next = Node(value, None)
    return head
# unfinished
#def merge_lists(a_head, b_head):
#    if b_head == None:
#        return a_head
#    a_head = add_ordered(a_head, b_head.value)
#    b_head = b_head.next

def reverse(head):
    if head == None or head.next == None:
        return head
        
    node = reverse(head.next)
    end = getEnd(node)
    end.next = head
    head.next = None
    return node
    
# created list
head1 = Node(1, None)
head1 = add_end(head1, 3)
head1 = add_end(head1, 5)

head2 = Node(2, None)
head2 = add_end(head2, 4)
head2 = add_end(head2, 6)

print_list(head2)
head = None
# Length
print(lenght_recursive(head))
print(lenght_iteratively(head))

# Sum
print(sum_recursive(head))
print(sum_iteratively(head))
# Insert right pos
head = add_ordered(head, 4)
head = add_ordered(head, 3)
head = add_ordered(head, 4)
head = add_ordered(head, 10)
head = add_ordered(head, 11)
head = add_ordered(head, 9)
head = add_ordered(head, 11)
print_list(head)
head = reverse(head)
print_list(head1)
print_list(head2)
print_list(head)
# unfinished
# head3 = merge_lists(head1, head2)
# print("Merged List")
# print_list(head3)