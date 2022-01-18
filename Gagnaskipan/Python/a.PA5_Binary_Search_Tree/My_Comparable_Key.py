
class MyComparableKey():
    def __init__(self, int_value, string_value):
        """ A constructor that takes an integer value and a string value. """
        self.int_value = int_value
        self.string_value = string_value


    def __lt__(self, other):
        """ Compares two instances of MyComparableKey and returns 
            ​True if the value of self is lower, otherwise ​False​. 
            A key value is considered lower if the ​integer​ value is lower. 
            In case of ​equal integers​ the order of the ​strings​ is used. """
        if self.int_value != other.int_value:
            return self.int_value < other.int_value
        else:
            return self.string_value < other.string_value

