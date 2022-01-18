class TestArray():
    def __init__(self):
        self.instanceOfArray = Array() 

    def testAdd(self):
        self.instanceOfArray.add(1)
        try:
            assert str(self.instanceOfArray) == "1"
            self.instanceOfArray.add(15)
            assert str(self.instanceOfArray._arr) == "1 15"
        except AssertionError:
            print("Add function does not work!")
        self._reset()
    
    def testDuplicates(self):
        self.instanceOfArray.add(1)
        self.instanceOfArray.add(1)
        self.instanceOfArray.add(2)
        self.instanceOfArray.add(2)
        self.instanceOfArray.add(3)
        self.instanceOfArray.add(3)
        self.instanceOfArray.removeDuplicates()
        try:
            assert str(self.instanceOfArray) == "1 2 3"         
        except AssertionError:
            print("removeDuplicates function does not work!")
        self._reset()
    
    def testString(self):
        try:
            assert str(self.instanceOfArray) == ""
        except AssertionError:
            print("String function does not work!")
        self.instanceOfArray.add(1)
        self.instanceOfArray.add("1")
        self.instanceOfArray.add(8)
        try:
            assert str(self.instanceOfArray) == "1 1 8"
        except AssertionError:
            print("String function does not work!")
        self._reset()

    def _reset(self):
        self.instanceOfArray = Array()


class Array():

    def __init__(self):
        # Creates an empty list and implement the variables; 
        #   size, array, capacity
        pass
    
    def add(self, data):
        # check if size is equal or bigger than capacity
        # always adds the data to the size of the array
        # lastly add one to size variable
        pass
    
    def removeDuplicates(self):
        # loops through the array twice and checks if any data in the array are equal
        # Checks should go:
        #   index 0 == index 1
        #   index 0 == index 2
        #   index 0 == index self.size-1

        #   index 1 == index 2
        #   ...
        #   index 1 == index self.size-1
        
        #   index self.size-2 == index self.size-1
        #   End of loops
        
        # if the array has the same items then
        # move every item (that is in front of the item) after it one step forward and check the same if statment again.
        pass

    def moveForward(self, index):
        # moves the item in an array one step forward
        pass

    def __getitem__(self, index):
        # gets the i-th item in the array
        return self._arr[index]

    def resize(self):
        # doubles the capacity of the array
        pass

    def __str__(self):
        # returns string with the items
        return ""
    

a = Array()

test = TestArray()
test.testAdd()
test.testDuplicates()
test.testString()