class Node:
    def __init__(self, data = None, _next = None):
        self.data = data
        self.next = _next

#    def get_next(self):
#        return self.next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


# def getEnd(head):
#     while head.get_next() != None:
#         head = head.next
#     return head

def palindrome(head):
    pass



#    if head == None or head.next == None:
#        return True       
#    else:
#        node = palindrome(head.next)
#        end = getEnd(node)
#        end.next = head
#        head.next = None
#        return node
#    
#    if node == end:
#        return True
#    else:
#        return False

#    if head == None or head.next == None:
#        return True
#    if head[0] != head[-1]:
#        return False
#    return palindrome(head[1:-1])




if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")