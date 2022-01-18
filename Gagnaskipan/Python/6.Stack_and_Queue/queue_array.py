
class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity
        self.front = 0
        self.back = 0

    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        avail = (self.front + self.size) % self.capacity
        self.arr[avail] = value
        self.size += 1

    def remove(self):
        if self.capacity <= 1:
            return "No value in the list to remove."
        else:
            return_val = self.arr[self.front]
            self.arr[self.front] = 0
            self.front += 1
        return return_val


    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for x in range(0, self.size):
            new_arr[x] = self.arr[x]
        self.arr = new_arr



queue = Queue(4)
queue.add(3)
queue.add(5)
queue.add(7)
queue.add(9)
queue.add(11)
remove = queue.remove()
print(remove)
            



class Queue2():
    def __init__(self):
        self.capacity = 4
        self.arr = [0] * self.capacity
        self.size = 0
        
    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        for i in self.arr:
            if i == 0:
                i = value
                self.size += 1
                return
        
    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in self.arr:
            new_array[i] = self.arr[i]
        self.arr = new_array
        
    def remove(self):
        for i in range(self.size):
            self.arr[i] = self.arr[i+1]
        self.size -= 1

    def __str__(self):
        ret_str = ""
        for i in self.arr:
            ret_str += str(i) + " "
        return ret_str


queue2 = Queue2()
queue2.add(2)
queue2.add(4)
queue2.add(3)
queue2.add(5)
queue2.add(8)
print(queue2)