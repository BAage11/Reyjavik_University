def get_list(lenght):
    row = 0
    ticlist = []
    line_list = []
    while lenght >= 3 and row < lenght: 
        line_list =[]
        for x in range(lenght):
            x = x + 1
            formula = (x) + (lenght * row)
            line_list.append(str(formula))
            if x == lenght:
                break
        ticlist.append(line_list)
        row += 1
    return ticlist

def board_print(ticlist):
    for inner_list in ticlist:
        for inner_inner_list in inner_list:
            print("{:>5s}".format(inner_inner_list), end="")
        print()

def playerA(ticlist):
    guess = input('Position: ')
    for rows in ticlist:
        for index, items in enumerate(rows):
            if guess == items:
                rows[index] = 'X'
                return ticlist

def playerB(ticlist):
    guess = input('Position: ')
    for rows in ticlist:
        for index, items in enumerate(rows):
            if guess == items:
                rows[index] ='O'
                return ticlist  

def victory(ticlist, lenght):
    counter = 0
    victory_list = []
    while counter < lenght:
        for letters in ticlist[counter]:
            if letters == 'X':
                victory_list.append(letters)
                if len(victory_list) == lenght:
                    return True
            else:
                return False
                

# Main program starts here:
lenght = int(input('Input dimension of the board: '))
ticlist = get_list(lenght)
board_print(ticlist)
while victory(ticlist, lenght) == False:
    player_one = playerA(ticlist)
    board_print(ticlist)
    player_two = playerB(ticlist)
    board_print(ticlist)
