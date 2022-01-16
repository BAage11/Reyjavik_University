# Write a class called RockGuitars() that has attributes: 'guitarist' and 'guitar'. It has a constructor with three parameters, self, guitarist and guitar. The default value of guitarist and guitar should be empty string.
# The class should have __str__ method to return a string for output using this format: "{:<20s} {:<20s}". Lastly, it has the following method to set guitarist and guitar:
# set_entry(guitarist, guitar): both 'guitarist' and 'guitar' are strings.  'guitar" has the default value as the empty string. 

class RockGuitars():
  def __init__(self, guitarist="", guitar=""):
    self.guitarist = guitarist
    self.guitar = guitar

  def set_entry(self, guitarist, guitar=""):
    self.guitarist = guitarist
    self.guitar = guitar

  def __str__(self):
    return ("{:<20s} {:<20s}".format(self.guitarist, self.guitar))


g1 = RockGuitars()
g1.set_entry("Jimmy Page", "Gibson Les Paul Standard")
g2 = RockGuitars()
g2.set_entry("Angus Young", "Jaydee SG")
g3 = RockGuitars()
g3 = RockGuitars("Mark Knoppfler")
print(g1)
print(g2)
print(g3)