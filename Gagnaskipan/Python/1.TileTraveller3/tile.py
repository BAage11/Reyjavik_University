
class Tile():
    def __init__(self, west_wall = False, south_wall = False, coins = 0):
        self.west_wall = west_wall
        self.south_wall = south_wall
        self.coins = coins
    
    def are_coins(self):
        if self.coins > 0:
            return True
        else:
            return False

    def get_coins(self):
        if self.coins > 0:
            self.coins -= 1
            return 1
        else:
            return 0
    