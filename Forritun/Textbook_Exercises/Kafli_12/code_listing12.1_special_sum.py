# Blaðsíða 611 - Code listing 12.2

class MyClass(object):
  def __init__(self, param1=0):
    """ constructor, sets attribute value to param1, default is 0 """
    print("in constructor")
    self.value = param1
  
  def __str__(self):
    """ Convert val attribute to string. """
    print("in str")
    return "Val is: {}".format(str(self.value))

  def __add_(self, param2):
    """ Perform addition with param2, a MyClass instance.
    Return a new MyClass instance with sum as value attribute """
    print("in add")
    result = self.value + param2.value
    return MyClass(result)


inst1 = MyClass(27)
type(inst1)
print("-"*20)

print(inst1)            # calls __str__
print("-"*20)

# a_sum = inst1 + inst1   # calls __add__
# print(a_sum)
# 
# print("-"*20)
# type(a_sum)
