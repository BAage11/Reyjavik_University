
class Node():
    def __init__(self):
        self.data = None
        self.next = None


head = Node()
head.data = "string 1"

node = head
for i in range(2, 6):
    node.next = Node()
    node = node.next
    node.data = "string " + str(i)

node = head
while node != None:
    print(node.data)
    node = node.next