# Write a class called Rectangle. A Rectangle should have two private attributes that represent the __length and __width of the rectangle.
# You should be able to create A Rectangle instance by supplying a values for its __length and its __width(in that order). If no arguements are given the default value 0 should be set for both attributes.
# Also, if a negative number is passed as an argument it should default to zero.
# You should implement the following methods on the class:
# area() returns the area of the Rectangle
# perimeter() returns the perimeter of the rectangle
# __str__() which should print the the __length and __width of the rectangle like this "Length: 2, __Width: 4" where 2 and 4 are the values that were supplied when the Rectangle was created.
# You should be able to check whether two Rectangle instances are equal by using the == operator. Two Rectangles are equal if the have the same area.
# You should also implement the __repr__() method. If a Rectangle has a __length of 10 and a __width of 2 this method should return a string like this: "Rectangle(10, 2)"

class Rectangle():
  def __init__(self, length=0, width=0):
    if length < 0:
      length = 0
    if width < 0:
      width = 0
    self.__length = length
    self.__width = width

  def __eq__(self, other):
    if self.area() == other.area():
      return True
    else:
      return False

  def area(self):
    """ Returns the area of the rectangle. """
    return (self.__length * self.__width)

  def perimeter(self):
    """ Returns the perimeter of the rectangle. """
    return (self.__length * 2 + self.__width * 2)

  def __str__(self):
    """ Prints the __length and __width of the rectangle. """
    return "Length: {}, Width: {}".format(self.__length, self.__width)
  
  def __repr__(self):
    """ Returning a different format, if rectangle is of __length 10 and __width 2. """
    return "Rectangle({},{})".format(self.__length, self.__width)


a = Rectangle()
b = Rectangle(2,3)
print(a)
print(a.area())
print(a.perimeter())
print(a.__repr__())
print(a == b)