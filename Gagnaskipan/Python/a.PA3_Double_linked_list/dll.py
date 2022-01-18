
class Node():
    def __init__(self, data=None, prev=None, _next=None):
        self.data = data
        self.prev = prev
        self.next = _next


class DLL():
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        self.current_node = self.trailer
        self.index = 0

    def __str__(self):
        current_node = self.header.next
        ret_str = ""
        while current_node.data != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next
        return ret_str

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, value):
        new_node = Node(value, self.current_node.prev, self.current_node)
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.current_node = new_node
        self.size += 1

    def remove_between(self, prev_node, next_node):
        if self.size == 0:
            return
        elif prev_node == None:
            next_node.prev = self.header
            self.size -= 1
        elif next_node == None:
            prev_node.next = self.trailer
            self.size -= 1
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
            self.size -= 1

    def remove(self):
        if self.is_empty() == False and self.current_node.next != None:
            self.remove_between(self.current_node.prev, self.current_node.next)
            self.current_node = self.current_node.next

    def get_value(self):
        if self.current_node == None:
            return None
        else:
            return self.current_node.data

    def move_to_next(self):
        if self.current_node.next != None:
            self.current_node = self.current_node.next
            self.index += 1

    def move_to_prev(self):
        if self.current_node.prev.prev != None:
            self.current_node = self.current_node.prev
            self.index -= 1

    def move_to_pos(self, position):
        if position < 0:
            return
        elif position > self.size:
            return
        count = 0
        curr = self.header.next
        while count != position:
            count += 1
            curr = curr.next
        self.current_node = curr
        self.index = position
        
    def remove_all(self, value):
        next_value = self.header.next
        index = 0
        boolean = False
        while next_value.next != None:
            if next_value.data == value:
                if index == self.index:
                    boolean = True
                self.remove_between(next_value.prev, next_value.next)
            next_value = next_value.next
            index += 1
        if boolean == True:
            self.current_node = self.header.next
            self.index = 0

    def reverse(self):
        tmp = None
        current_item = self.header
        while current_item != None:                 
            tmp = current_item.prev  
            current_item.prev = current_item.next       # Flips the pointer
            current_item.next = tmp                     # Flips the other pointer of the node
            current_item = current_item.prev  
            # Takes the next item (to the right) in the list
        if tmp != None:
            self.header = tmp.prev
            # Change the head so the old last item will now be the header of the list
        self.current_node = self.header.next
        self.index = 0

    def sort(self):
        compare = self.header.next    
        pivot = self.header.next       
        current = self.header.next    
        while pivot.next != None:
            while current.prev.prev != None:
                if current.data < compare.data:
                    self.swap(current, compare)
                    compare = compare.prev
                    current = current.prev
                else:
                    break
            pivot = pivot.next
            current = pivot
            compare = pivot.prev
        self.current_node = self.header.next
        self.index = 0

    def swap(self,item1, item2):
        item1.data, item2.data = item2.data, item1.data


# dll = DLL()
# print("\nEmpty list:")
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nInsert into list:")
# dll.insert("A")
# dll.insert("B")
# dll.insert("1")
# dll.insert("4")
# dll.insert("C")
# dll.insert("9")
# dll.insert("B")
# dll.insert("6")
# dll.insert("3")
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nRemove items from list:")
# dll.remove()
# dll.remove()
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nMove compare node further back:")
# dll.move_to_next()
# dll.move_to_next()
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nMove compare node further front:")
# dll.move_to_prev()
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nMove compare node to another position in the list:")
# dll.move_to_pos(6)
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nRemove all instances of value:")
# dll.remove_all("B")
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nReverse the order of items in list (and compare node is now at the first node)")
# dll.reverse()
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# print("\nSort the items in list (and compare node is now at the first node):")
# dll.sort()
# print("The list:", dll)
# curr_node = dll.get_value()
# print("Current node:", curr_node)
# print("Length of list:", len(dll))
# 
# 