from Double_Linked_List import Double_Linked_List, Empty

class DLL_Deque(Double_Linked_List):
    def get_first(self):
        if self.is_empty():
            raise Empty
        return self.header._next.data

    def get_last(self):
        if self.is_empty():
            raise Empty
        return self.trailer.prev.data

    def insert_between(self, data, before, after):
        # Item before 'new_item' == 'before'
        # item after 'new item' == 'after'
        new_item = self.Node(data, before, after)
        before._next = new_item
        after.prev = new_item
        self._size += 1
        return new_item

    def add_first(self, data):
        self.insert_between(data, self.header, self.header._next)

    def add_last(self, data):
        self.insert_between(data, self.trailer.prev, self.trailer)

    def delete_node(self, data):
        before = data.prev      # Ná í gildið sem kemur eftir 'data'
        after = data._next       # Ná í gildið sem kemur á undan 'data'
        before._next = after     # Breyta gildi á eftir 'before' í 'after'
        after.prev = before     # Breyta gildi á undan 'after' í 'before'
        # Þar með er gildið 'data' ekki lengur með tengsl við listann
        self._size -= 1
        
    def remove_first(self):
        if self.header._next == None:
            raise Empty
        else:
            self.delete_node(self.header._next)

    def remove_last(self):
        if self.header._next == None:
            raise Empty
        else:
            self.delete_node(self.trailer.prev)

    def __str__(self):
        current_node = self.header._next
        ret_str = ""
        while current_node.data != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node._next
        return ret_str


deque = DLL_Deque()
print(deque)

deque.add_first(11)
deque.add_first(22)
deque.add_first(33)
print(deque)

deque.add_last(44)
deque.add_last(55)
deque.add_last(66)
print(deque)

first_item = deque.get_first()
print(first_item)

last_item = deque.get_last()
print(last_item)

deque.remove_first()
print(deque)

deque.remove_last()
print(deque)