
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)   
        # Viljum hafa þetta aftast og notum því default gildið í klasanum Node(), það er 'None' fyrir self.next. Þ.a.l. setjum við einungis hér inn 'data'.
        if self.head == None:           # Er listinn tómur?
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        
    def __str__(self):
        ret_str = ""
        current_node = self.head
        while current_node != None:
            ret_str += str(current_node.data) + ", "
            current_node = current_node.next
        return ret_str[:-2]

# Verið að bæta framan við listann hér, en ekki aftan við listann eins og í 'nytt1.py'
def push_front(head, data):
    new_node = Node(data, head)
    return new_node


a_list = LinkedList()
for i in range(1, 6):
    a_list.push_back("string " + str(i))

print(a_list)














# head = Node()
# head.data = "string 1"
# for i in range(2, 6):
#     head = push_front(head, "string " + str(i))
# 
# 
# node = head
# while node != None:
#     print(node.data)
#     node = node.next
