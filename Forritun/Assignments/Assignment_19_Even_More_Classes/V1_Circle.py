# Implement the class Circle which has a private member variable for radius. Implement the member functions needed for the following program to run:
# You will need to use the constant PI = 3.14159 in your  program. Find out how to use it from the math module.

import math

class Circle():
  def __init__(self, radius):
    self.__radius = float(radius)    
    # Private - Ekki aðgengilegt fyrir notendur klasans
    # Ekki hægt til dæmis að gera skipunina "Circle.radius"
  
  def __str__(self):
    return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.area(), self.perimeter())
  
  def area(self):
    return math.pi * self.__radius**2
    # Kemst í __radius af því það er enn verið að vinna inní klasanum, ekki utan hans.

  def perimeter(self):
    return 2 * math.pi * self.__radius

  def get_radius(self):
    return self.__radius

  def set_radius(self, new_radius):
    self.__radius = new_radius
    return self.__radius


def main():   
  radius = input("Radius of circle: ")        
  circle = Circle(radius)
  print(circle)
  circle.set_radius(circle.get_radius() + 1.0)   
  print(circle)

main()