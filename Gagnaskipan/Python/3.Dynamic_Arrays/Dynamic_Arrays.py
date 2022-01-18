import random

class ArrayList():
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

        while self.capacity != self.size:
            self.value = random.randint(0, 100)
            self.append(self.arr, self.value)
                
        self.print_array_list(self.arr)
        print("get_first:", self.get_first(self.arr))
        print("get_at:", self.get_at(self.arr, 2))
        print("get_last:", self.get_last(self.arr))
        self.resize(self.arr)
        print("resize:", self.arr)
        print("prepend:", self.prepend(self.arr, 99))
        print("insert:", self.insert(self.arr, 88, 7))
        self.remove(self.arr, 2)


    def print_array_list(self, array_list):
        print_str = ""
        for i in array_list:
            if i != 0:
                print_str += str(i) + ", "
        print(print_str[:-2])


    def append(self, array_list, value):
        array_list[self.size] = self.value
        self.size += 1

        
    def get_first(self, array_list):
        return array_list[0]


    def get_at(self, array_list, index):
        return array_list[index]


    def get_last(self, array_list):
        return array_list[-1]


    def resize(self, array_list):
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def prepend(self, array_list, value):
        for i in array_list:
            pass
        

    def insert(self, array_list, value, index):
        pass
    
    def remove(self, array_list, index):
        for i in array_list:
            if i == index:
                while index+1 != 0:
                    self.arr[i] == self.arr[i+1]
        print("remove:", self.arr)




ArrayList()
