
class Vehicle(object):
  def __init__(self, the_license="", the_year=0, weight=0.0, fee=0.0):
    self.the_license = the_license
    self.the_year = the_year
    self.weight = weight
    self.fee = fee

  def get_license(self):
    return self.the_license

  def get_year(self):
    return self.the_year

  def get_weight(self):
    return self.weight

  def get_fee(self):
    return self.fee

  def __str__(self):
    return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.weight, self.fee)


class Car(Vehicle):    # subclass
  def __init__(self, the_license, the_year, the_style):
    Vehicle.__init__(self, the_license, the_year, weight=0.0, fee=0.0)
    self.the_style = the_style

  def get_weight(self):
    return self.weight

  def set_weight(self, weight=0.0):
    self.weight = weight
    if self.weight < 3000:
      self.fee = 30
    elif self.weight >= 3000 and self.weight < 5000:
      self.fee = 40
    else:
      self.fee = 50
    return self.fee

  def __str__(self):
    return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.the_style, self.weight, self.fee)


class Truck(Vehicle):    # subclass
  def __init__(self, the_license, the_year, the_wheels):
    Vehicle.__init__(self, the_license, the_year, weight=0.0, fee=0.0)
    self.the_wheels = the_wheels  

  def set_weight(self, weight=0.0):
    self.weight = weight
    if self.weight < 3000:
      self.fee = 40
    elif self.weight >= 3000 and self.weight < 5000:
      self.fee = 50
    elif self.weight >= 5000 and self.weight < 10000:
      self.fee = 60
    else:
      self.fee = 70
    return self.fee

  def __str__(self):
    return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.the_wheels, self.weight, self.fee)


class Motorbike(Vehicle):    # subclass
  def __init__(self, the_license, the_year, cc=0):
    Vehicle.__init__(self, the_license, the_year, weight=0.0, fee=0.0)
    self.cc = cc

  def get_CC(self):
    return self.cc

  def set_CC(self, cc=0):
    self.cc = cc
    if self.cc < 50:
      self.fee = 10
    elif self.cc >= 50 and self.cc < 200:
      self.fee = 20
    else:
      self.fee = 35
    return self.fee

  def __str__(self):
    return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.the_license, self.the_year, self.cc, self.fee)


######################################################################

# Main program starts here:
def main():
  # Create some vehicles
  v1 = Vehicle("AB 123", 2010)
  c1 = Car("SF 735", 2007, "Station")
  t1 = Truck("TU 765", 1994, 6)
  b1 = Motorbike("XY 666", 2005)

  c1.set_weight(3500)
  t1.set_weight(9000)
  b1.set_CC(250)

  # Print info
  print(v1)
  print(c1)
  print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
  print(t1)
  print("The fee for the truck is: {:.2f}".format(t1.get_fee() )) 
  print(b1)
  print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
  print()

  # Put the four vehicles into a list.
  # Then loop through the list and call the print function for each of the vehicles.
  # You have to implement this part of the main program!
  the_list = [v1, c1, t1, b1]
  for i in the_list:
    print(i)


  print(c1)

main()


