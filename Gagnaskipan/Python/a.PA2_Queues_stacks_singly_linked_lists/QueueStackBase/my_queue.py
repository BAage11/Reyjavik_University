from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, _type=""):
        self.data = _type
        if self.data == "linked":
            self._type = LinkedList()
        elif self.data == "array":
            self._type = ArrayDeque()

    def add(self, value):
        if self.data == "linked":
            self._type.push_back(value)
        elif self.data == "array":
            self._type.push_back(value)

    def remove(self):
        if self._type.size == 0:
            return None
        elif self.data == "linked":
            value = self._type.pop_front()
        elif self.data == "array":
            value = self._type.pop_front()
        return value

    def get_size(self):
        return self._type.size

