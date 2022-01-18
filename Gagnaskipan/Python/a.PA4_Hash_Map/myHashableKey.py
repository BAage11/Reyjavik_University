
class MyHashableKey():
    def __init__(self, int_value, string_value):
        """ A constructor that takes an integer value and a string value. """
        self.integer_value = int_value
        self.string_value = string_value


    def __eq__(self, other):
        """ Compares two instances of MyHashableKey.
            Returns True if their values are equal, otherwise False. """
        return self.__dict__ == other.__dict__

    
    def __hash__(self):
        """ Returns an integer. The integer value must be the same for 
            instances that are equal. Otherwise can be any integer. """ 
        string = self.string_value
        sum = abs(self.integer_value)
        for i in string:
            sum += ord(i)
        return sum

