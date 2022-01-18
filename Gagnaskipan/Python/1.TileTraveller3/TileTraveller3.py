import position
from position import *

import grid
from grid import *

class TileTraveller():
    def __init__(self):
        self.points = 0
        self.position = Position(0, 0)
        self.grid = Grid(4, 3)

    def play_game(self):
        print("\nEnter Q at any time to quit.")
        while True:
            if self.grid.is_in_end(self.position):
                print("\nYou have won!!!\nYou got {} coins!\n\n".format(self.points))
                self.position = Position(0, 0)
                self.grid = Grid(4, 3)

            print(self.grid.get_possibilities(self.position))
            input_str = input("Enter your choice: ")
            
            if input_str == "Q" or input_str == "q":
                exit()
            elif input_str == "G" or input_str == "g":
                got_coins = self.grid.get_coins(self.position)
                self.points += got_coins
                if got_coins > 0:
                    print("You found " + str(got_coins) + " coin(s)!")
                else:
                    print("There are no coins!")
            else:
                print(self.grid.move(self.position, input_str))
        


tile_traveller = TileTraveller()
tile_traveller.play_game()



#        print(self.grid.move(self.position, "E"))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.move(self.position, "W"))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.move(self.position, "W"))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.move(self.position, "S"))

#        print(self.grid.move(self.position, "E"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "W"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "W"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "N"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "E"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.get_possibilities(self.position))
#        print(self.grid.move(self.position, "S"))
#        print(self.grid.get_possibilities(self.position))