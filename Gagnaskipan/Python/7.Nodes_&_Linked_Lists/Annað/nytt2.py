
class Node():
    def __init__(self):
        self.data = None
        self.next = None


# Verið að bæta framan við listann hér, en ekki aftan við listann eins og í 'nytt1.py'
def push_front(head, data):
    new_node = Node()
    new_node.data = data
    new_node.next = head        
    # head verður next, þar sem verið er að setja stakk framan við með "new node"
    # Síðan er gert 'head = new_node' ef þetta væri inn í klasanum, en annars....
    return new_node


head = Node()
head.data = "string 1"
for i in range(2, 6):
    head = push_front(head, "string " + str(i))


node = head
while node != None:
    print(node.data)
    node = node.next