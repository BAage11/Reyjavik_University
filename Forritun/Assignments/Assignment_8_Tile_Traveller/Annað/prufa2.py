NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"

def move(direction, row, column):
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        column += 1
    elif direction == WEST:
        column -= 1



victory = False
row = 1
column = 1

print("You can travel: N(orth).")
valid_direction = NORTH

while victory == False:
    v
    
    direction = input("Direction: ").lower()

    if direction not in valid_direction:
        print("Not a valid direction!")
    else:
        

        if row == 1 and column == 3:
            print("Victory!")
            victory = True
        else:
            print("You can travel:", end=" ")
            if row == 1 and column == 1:
                print("N(orth).")
                valid_direction = NORTH
            elif row == 1 and column == 2:
                print("N(orth).")
                valid_direction = NORTH
            elif row == 2 and column == 1:
                print("N(orth) or S(outh) or E(ast).")
                valid_direction = NORTH+SOUTH+EAST
            elif row == 2 and column == 2:
                print("S(outh) or W(est).")
                valid_direction = SOUTH+WEST
            elif row == 2 and column == 3:
                print("N(orth) or S(outh).")
                valid_direction = NORTH+SOUTH
            elif row == 3 and column == 1:
                print("S(outh) or E(ast).")
                valid_direction = SOUTH+EAST
            elif row == 3 and column == 2:
                print("W(est) or E(ast).")
                valid_direction = EAST+WEST
            elif row == 3 and column == 3:
                print("S(outh) or W(est).")
                valid_direction = SOUTH+WEST

        