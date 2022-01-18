class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def getEnd(head):
    while head.get_next() != None:
        head = head.next
    return head

def reverse(head):
    if head == None or head.next == None:
        return head        
    node = reverse(head.next)
    end = getEnd(node)
    end.next = head
    head.next = None
    return node

def split_in_half(first, second):
    if second == None or second.next == None or second.next.next == None:
        return first
    else:
        first = first.next
        second = second.next.next
    return split_in_half(first, second)
    
def check(head, reversed_head):
    if reversed_head == None or head == None:
        return True
    else:
        if head.data == reversed_head.data:
            return check(head.next, reversed_head.next)
        else:
            return False
    
def palindrome(head):
    second_half = split_in_half(head, head)
    second_half_next = second_half.next
    reversed_second_half = reverse(second_half_next)
    bool_value = check(head, reversed_second_half)
    second_half.next = reverse(reversed_second_half)
    return bool_value



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
