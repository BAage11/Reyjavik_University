# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

victory = False
row = 1
col = 1

print("You can travel: (N)orth.")
valid_directions = NORTH

while not victory:
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        if direction == NORTH:
            row += 1
        elif direction == SOUTH:
            row -= 1
        elif direction == EAST:
            col += 1
        elif direction == WEST:
            col -= 1
    
        if col == 3 and row == 1: # (3,1)
            print("Victory!")
            victory = True
        else:
            print("You can travel: ", end='')
            if col == 1 and row == 1:   # (1,1)
                print("(N)orth.")
                valid_directions = NORTH
            elif col == 1 and row == 2: # (1,2)
                print("(N)orth or (E)ast or (S)outh.")
                valid_directions = NORTH+EAST+SOUTH
            elif col == 1 and row == 3: # (1,3)
                print("(E)ast or (S)outh.")
                valid_directions = EAST+SOUTH
            elif col == 2 and row == 1: # (2,1)
                print("(N)orth.")
                valid_directions = NORTH
            elif col == 2 and row == 2: # (2,2)
                print("(S)outh or (W)est.")
                valid_directions = SOUTH+WEST
            elif col == 2 and row == 3: # (2,3)
                print("(E)ast or (W)est.")
                valid_directions = EAST+WEST
            elif col == 3 and row == 2: # (3,2)
                print("(N)orth or (S)outh.")
                valid_directions = NORTH+SOUTH
            elif col == 3 and row == 3: # (3,3)
                print("(S)outh or (W)est.")
                valid_directions = SOUTH+WEST
        