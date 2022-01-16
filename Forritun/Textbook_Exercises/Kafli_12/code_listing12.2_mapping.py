# Blaðsíða 611 - Code listing 12.2

class MyClass(object):
  def __init__(self, param1=0):
    """ constructor, sets attribute value to param1, default is 0 """
    self.value = param1

  def __str__(self):
    """ Convert val attribute to string. """
    return "Val is: {}".format(str(self.value))

  def __add__(self, param2):
    """ Perform addition with param2, a MyClass instance. 
    Return a new MyClass instance with sum as value attribute. """
    result = self.value + param2.value
    return MyClass(result)
  

inst1 = MyClass(27)
print(inst1)

a_sum = inst1 + inst1
print(a_sum)
