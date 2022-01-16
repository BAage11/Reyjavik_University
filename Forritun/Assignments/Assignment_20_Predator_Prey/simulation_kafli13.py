import random

class Island(object):
  def __init__(self, size, number_of_predators=0, number_of_prey=0):
    self.grid_size = size
    self.grid = []

    for _ in range(self.grid_size):
      row = [0]*size
      self.grid.append(row)

    self.populate_island(number_of_predators, number_of_prey)

  def __str__(self):
    s = ""
    for j in range(self.grid_size-1, -1, -1):
      for i in range(self.grid_size):
        if self.grid[i][j] == 0:
          s += "{:<2s}".format(".")
        else:
          s += "{:<2s}".format(str(self.grid[i][j]))
      s+= "\n"
    return s

  def set_animal_on_island(self, animal):
    self.grid[animal.x][animal.y] = animal

  def empty_cell(self, x, y):
    return self.grid[x][y] == 0 

  def reset_movement(self):
    for row in self.grid:
      for value in row:
        if isinstance(value, Animal):
          value.has_moved = False

  def populate_island(self, number_of_predators, number_of_prey):
    while number_of_predators > 0:
      x = random.randint(0, self.grid_size-1)
      y = random.randint(0, self.grid_size-1)

      if self.empty_cell(x,y):
        new_predator = Predator(self, x, y)
        self.set_animal_on_island(new_predator)
        number_of_predators -= 1

    while number_of_prey > 0:
      x = random.randint(0, self.grid_size-1)
      y = random.randint(0, self.grid_size-1)

      if self.empty_cell(x,y):
        new_prey = Prey(self, x, y)
        self.set_animal_on_island(new_prey)
        number_of_prey-= 1

  def remove_animal(self, animal):
    self.grid[animal.x][animal.y] = 0

  def within_grid(self, x, y):
    return 0 <= x < self.grid_size and 0 <= y < self.grid_size

class Animal(object):
  def __init__(self, island, x=0, y=0, name="A"):
    self.island = island
    self.x = x
    self.y = y
    self.name = name
    self.has_moved = False

  def __str__(self):
    return self.name

  def get_new_position(self, target=int):
    offset_list = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
    for coord in offset_list:
      new_x = self.x + coord[0]
      new_y = self.y + coord[1]
      if self.island.within_grid(new_x, new_y) and isinstance(self.island.grid[new_x][new_y], target):
        return (new_x, new_y)
    return None

  def move(self):
    if not self.has_moved:
     new_position = self.get_new_position()
     if new_position != None:
        self.island.remove_animal(self)
        self.x, self.y = new_position
        self.island.set_animal_on_island(self)
        self.has_moved = True

class Predator(Animal):
  def __init__(self, island, x=0, y=0, name="R"):
    Animal.__init__(self, island, x, y, name)

  def eat(self):
    if not self.has_moved:
      new_position = self.get_new_position(Prey)
      if new_position != None:
        self.island.remove_animal(self)
        self.x, self.y = new_position
        self.island.set_animal_on_island(self)
        self.has_moved = True

class Prey(Animal):
  def __init__(self, island, x=0, y=0, name="B"):
    Animal.__init__(self, island, x, y, name)

########################################################

def main():
  tenerife = Island(5, 5, 10)
  turns = 10
  while turns > 0:
    print(tenerife)
    for x in range(tenerife.grid_size):
      for y in range(tenerife.grid_size):
        if isinstance(tenerife.grid[x][y], Animal):
          animal = tenerife.grid[x][y]
          if isinstance(animal, Predator):
            animal.eat()
          animal.move()     
    tenerife.reset_movement()     
    turns -= 1
    print(tenerife)


main()
