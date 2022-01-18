import tile
from tile import *

import position
from position import *

class Grid():
    def __init__(self, width = 3, height = 3):
        self.width = width
        self.height = height
        self.tiles = None
        self.buildMaze(width, height)


    def buildMaze(self, width = 3, height = 3):
        self.width = width
        self.height = height
        self.tiles = []
        for i in range(self.width):
            self.tiles.append([])
            for _ in range(self.height):
                self.tiles[i].append(Tile())

        self.tiles[1][2].south_wall = True
        self.tiles[2][1].west_wall = True 
        self.tiles[1][0].west_wall = True       
        self.tiles[2][0].west_wall = True   
        self.tiles[2][2].south_wall = True   
        self.tiles[3][1].south_wall = True   

        self.tiles[0][1].coins = 1
        self.tiles[1][0].coins = 3    
        self.tiles[2][0].coins = 1
        self.tiles[3][2].coins = 2


    def can_go(self, position, input_str):
        if input_str == "N":
            if (position.y >= 0 and position.y + 1 < self.height
            and position.x >= 0 and position.x < self.width 
            and self.tiles[position.x][position.y + 1].south_wall == False):
                return True
        
        elif input_str == "S":
            if (position.y > 0 and position.y < self.height
            and position.x >= 0 and position.x < self.width 
            and self.tiles[position.x][position.y].south_wall == False):
                return True
        
        elif input_str == "E":
            if (position.y >= 0 and position.y < self.height
            and position.x >= 0 and position.x + 1 < self.width 
            and self.tiles[position.x + 1][position.y].west_wall == False):
                return True
        
        elif input_str == "W":
            if (position.y >= 0 and position.y < self.height
            and position.x > 0 and position.x < self.width 
            and self.tiles[position.x][position.y].west_wall == False):
                return True
        return False


    def move(self, position, input_str):
        if (input_str == "n" or input_str == "N"):
            if self.can_go(position, "N"):
                position.y += 1
                return "Moved North!"
            else:
                return "Can't move North!"
        
        elif (input_str == "s" or input_str == "S"):
            if self.can_go(position, "S"):    
                position.y -= 1
                return "Moved South!"
            else:
                return "Can't move South!"
        
        elif (input_str == "e" or input_str == "E"):
            if self.can_go(position, "E"):
                position.x += 1
                return "Moved East!"
            else:
                return "Can't move East!"
        
        elif (input_str == "w" or input_str == "W"):
            if self.can_go(position, "W"):
                position.x -= 1
                return "Moved West!"
            else:
                return "Can't move West!"
        else:
            "Invalid input!"

    def get_coins(self, position):
        return self.tiles[position.x][position.y].get_coins()
        

    def get_possibilities(self, position):
        ret_str = "\nPossibilities are:"
        if self.can_go(position, "N"):
            ret_str += "\nN: Go north"
        if self.can_go(position, "S"):
            ret_str += "\nS: Go south"
        if self.can_go(position, "E"):
            ret_str += "\nE: Go east"
        if self.can_go(position, "W"):
            ret_str += "\nW: Go west"
        if self.tiles[position.x][position.y].are_coins():
            ret_str += "\nG: Get coins"            
        return ret_str


    def is_in_end(self, position):
        if position.x == self.width - 1 and position.y == 0:
            return True
        else:
            return False