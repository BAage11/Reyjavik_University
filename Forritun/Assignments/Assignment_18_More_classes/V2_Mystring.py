# Write a class MyString() such that it has a method that gives the difference between the size of strings when the '-' (subtraction) operator is used between the two objects of the class. Additionally, implement a method that returns True if object 1 is greater than object 2 and False otherwise when the (>) (greater than) operator is used. Object 1 is greater than object 2 if the string it stores is longer than the string stored in object 2.

class MyString():
  def __init__(self, string=""):
    self.string = len(string)

  def __sub__(self, obj2):
    if self.string > obj2.string:
      return (self.string - obj2.string)
    else:
      return (obj2.string - self.string)

  def __gt__(self, obj2):
    if self.string > obj2.string:
      return True
    else:
      return False


obj1 = MyString("this is a string")
obj2 = MyString("this is another string")
print(obj1 > obj2)
print(obj1 - obj2)
