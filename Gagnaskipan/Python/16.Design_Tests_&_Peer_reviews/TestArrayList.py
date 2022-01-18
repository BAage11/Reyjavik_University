from ArrayDataStructure import *

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