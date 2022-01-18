class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class NotFound(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.is_sorted = True
        self.use_recursive_sort = True

    #Time complexity: O(n) - linear time in size of list
    def print(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        print(str_val)

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index > self.size or index < 0:
            return None
        if self.size >= self.capacity:
            self.resize()
        i = self.size
        while(i > index):
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[index] = value
        self.size += 1
        if self.size > 1:
            self.is_sorted = False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index >= 0 and index < self.size:
            self.arr[index] = value
            if self.size > 1:
                self.is_sorted = False

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(0)

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size > index and index >= 0:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(self.size - 1)

    #Time complexity: O(n) - linear time in size of list (but doesn't change time complexity of append or insert)
    def resize(self):
        tmp_arr = [0] * self.capacity * 2
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity *= 2

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.size > index and index >= 0:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i + 1]
            self.size -= 1
            if self.size <= 1:
                self.is_sorted = True

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.is_sorted = True

    #Time complexity: O(1) - constant time
    def swap_adjacent(self, index):
        tmp = self.arr[index]
        self.arr[index] = self.arr[index - 1]
        self.arr[index - 1] = tmp
        self.is_sorted = False

    #Time complexity: O(n^2) - quadratic time in size of list
    # because there's recursion down to the start of the list and then
    # it starts the recursion over until it's been done for every item
    def sort_recur(self, swap_index, sort_index):
        if swap_index >= 1 and self.arr[swap_index] < self.arr[swap_index - 1]:
            self.swap_adjacent(swap_index)
            self.sort_recur(swap_index - 1, sort_index)
        if sort_index + 1 < self.size:
            self.sort_recur(sort_index + 1, sort_index + 1)

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        self.append(value)
        if self.is_sorted == False:
            self.sort()
        else:
            self.sort_recur(self.size - 1, self.size - 1)

    #Time complexity: O(n^2) - quadratic time in size of list
    # because there's a loop over the size of list and
    # an inner loop over a linear function of the size
    def sort(self):
        if(self.is_sorted == True):
            return None
        if self.use_recursive_sort:
            self.sort_recur(1, 1)
        else:
            for i in range(1, self.size):
                index = i - 1
                while index >= 0 and self.arr[index] > self.arr[index + 1]:
                    self.swap_adjacent(index)
                    index -= 1
        self.is_sorted = True

    #Time complexity: O(log n) - logarithmic time in size of list
    # binary search
    def binary_search(self, value, left, right):
        if left == right:
            raise NotFound()
        index = (left + right) // 2
        if self.arr[index] == value:
            return index
        elif value < self.arr[index]:
            return self.binary_search(value, left, index)
        else:  #value > self.arr[index]
            return self.binary_search(value, index + 1, right)

    #Time complexity: O(n) - linear time in size of list
    # because it's a simple linear search
    def linear_search(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        raise NotFound()

    #Tima complexity dependant on if list is sorted
    def find(self, value):
        if self.is_sorted:
            return self.binary_search(value, 0, self.size)
        else:
            return self.linear_search(value)

    #Time complexity: O(n) - linear time in size of list
    # because it uses the linear search, then remove at,
    # both of which are O(n)
    def remove_value(self, value):
        try:
            self.remove_at(self.find(value))
        except NotFound:
            return None
        if(self.size <= 1):
            self.is_sorted = True
