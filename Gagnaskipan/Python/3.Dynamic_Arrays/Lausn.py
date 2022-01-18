class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    """ Double the array capacity """
    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for x in range(0, self.size):
            new_arr[x] = self.arr[x]
        self.arr = new_arr

    """ Prints the array """
    def print_array_list(self):
        string_builder = ""
        for x in range(0, self.size):
            if (self.size - 1) == x:
                string_builder += str(self.arr[x])
            else:
                string_builder += str(self.arr[x])
                string_builder += ", "
        print(string_builder)
    
    """ Appends to the end of the array """
    def append(self, value):
        if self.capacity == self.size:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    """ Inserts an element to the front of the arrays """
    def prepend(self, value):  
        if self.capacity == self.size:
            self.resize()
        for x in range(self.size - 1, -1, -1):
            temp_store = self.arr[x]
            self.arr[x + 1] = temp_store
        self.size += 1
        self.arr[0] = value
    
    """ Insert an element at an specific index """
    def insert(self, value, index):
        if index != self.size:
            self.check_valid_index(index)

        if self.capacity == self.size:
            self.resize()
        for x in range(self.size - 1, index - 1, -1):
            temp_store = self.arr[x]
            self.arr[x + 1] = temp_store
        self.arr[index] = value
        self.size += 1
    
    """ Removes an element at the selected index """
    def remove(self, index):
        self.check_valid_index(index)
        if self.size == self.capacity:
            self.resize()

        for x in range(index, self.size):
            if x != self.size:
                self.arr[x] = self.arr[x + 1]
        self.size -= 1

    """ Returns the first element of the array """
    def get_first(self):
        return self.arr[0]
    
    """ Returns the value at a specifc index of the array """
    def get_at(self, index):
        self.check_valid_index(index)
        return self.arr[index]
    
    """ Returns the last element of the array """
    def get_last(self):
        return self.arr[self.size - 1]
    
    """ Checks if the index supplied is within valid range """
    def check_valid_index(self, index):
        if index < 0 or index > self.size - 1:
            raise IndexError("Index value was out of range")
    
    # Extras

    """ Overrides value at index """
    def set_at(self, value, index):
        self.check_valid_index(index)
        self.arr[index] = value    

    """ Finds the first instance of a value and returns the index """
    def find(self, value):
        for x in range(0, self.size):
            if self.arr[x] == value:
                return x
        return None
    
    """ Finds multiple instances of a value and returns the indexes in an array """
    def find_multiple(self, value):
        return_array = Array(2)
        for x in range(0, self.size):
            if self.arr[x] == value:
                return_array.append(x)
        return return_array

    """ Removes the last element of the array """
    def pop_back(self):
        self.size -= 1

a = Array(4)
a.append(1)
a.append(2)
a.append(1)
a.append(4)
a.append(1)
a.append(6)
a.append(1)
a.prepend(8)
a.remove(1)
a.print_array_list()