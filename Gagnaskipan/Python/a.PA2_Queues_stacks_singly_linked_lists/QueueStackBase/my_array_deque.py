
class ArrayDeque():
    def __init__(self):
        self.capacity = 4
        self.deque = [0] * 4
        self.size = 0
        self.front = 0

    def push_back(self, value):
        if self.size >= self.capacity:
            self.resize()        
        index = (self.front + self.size) % self.capacity    
        # settur aftast (index) með því að reikna remainder (afgang)
        self.deque[index] = value
        self.size += 1

    def push_front(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.front = (self.front - 1) % self.capacity
        # front verður nú næsta index á undan í ArrayDeque
        self.deque[self.front] = value
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            return None
        self.size -= 1
        index = (self.front + self.size) % self.capacity
        # finnur aftasta index-ið með því að reikna remainder (afgang)
        value = self.deque[index]
        self.deque[index] = None
        return value

    def pop_front(self):
        if self.size == 0:
            return None
        value = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity
        # front verður nú á næsta indexi í ArrayDeque
        self.size -= 1
        return value

    def get_size(self):
        return self.size

    def resize(self):
        self.capacity *= 2
        larger_list = [0] * self.capacity
        next_item = self.front
        for i in range(self.size):
            larger_list[i] = self.deque[next_item]
            next_item = (1 + next_item) % self.size
        self.deque = larger_list
        self.front = 0

    def __str__(self):
        ret_str = ""
        value = self.front
        if value != 0:
            while value != self.capacity:
                if self.deque[value] == 0 or self.deque[value] == None:
                    value += 1
                    continue
                else:
                    ret_str += str(self.deque[value]) + " "
                    value += 1

            value = 0
            while value != self.front:
                if self.deque[value] == 0 or self.deque[value] == None:
                    value += 1
                    continue
                else:
                    ret_str += str(self.deque[value]) + " "
                    value += 1
        else:
            for i in range(self.capacity):
                if self.deque[i] == 0 or self.deque[i] == None:
                    continue
                else:
                    ret_str += str(self.deque[i]) + " "
        return ret_str

