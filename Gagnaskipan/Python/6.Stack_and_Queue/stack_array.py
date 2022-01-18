
class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity
        
    def push(self, value):
        if self.capacity == 0:
            return "List is empty."
        else:
            self.arr[self.size] = value
            self.size += 1
            if self.size == self.capacity:
                self.resize()  

    def pop(self):
        if self.capacity <= 1:
            return "No value in the list to pop off."
        else:
            value = self.arr[self.size-1]
            self.arr[self.size-1] = 0
            self.size -= 1
            return value

    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for x in range(0, self.size):
            new_arr[x] = self.arr[x]
        self.arr = new_arr


stack = Stack(4)
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(9)
stack.push(11)
pop = stack.pop()
print(pop)