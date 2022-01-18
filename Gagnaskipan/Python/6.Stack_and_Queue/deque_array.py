class Deque():
    def __init__(self):
        self.capacity = 4
        self.deque = [0] * 4
        self.size = 0
        self.front = 0
    
    def push_back(self, value):
        if self.size >= self.capacity:
            self.resize()

        avail = (self.front + self.size) % self.capacity
        self.deque[avail] = value
        self.size += 1
    
    def pop_back(self):
        if self.size <= 0:
            print("Deque is Empty!")
            quit()

        self.size -= 1
        avail = (self.front + self.size) % self.capacity
        self.deque[avail] = None

    def push_front(self, value):
        if self.size >= self.capacity:
            self.resize()

        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1

    def pop_front(self):
        if self.size <= 0:
            print("Deque is Empty!")
            quit()

        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
    
    def resize(self):
        self.capacity *= 2
        bigger_list = [0] * self.capacity
        next_ = self.front
        for i in range(self.size):
            bigger_list[i] = self.deque[next_]
            next_ = (1 + next_) % self.size
        self.deque = bigger_list
        self.front = 0



deque = Deque()

deque.push_back(1)
deque.push_back(2)

deque.push_front(3)

deque.push_back(4)
deque.push_back(5)

print(deque.deque)