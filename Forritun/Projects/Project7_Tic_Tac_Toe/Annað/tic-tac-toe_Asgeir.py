def validOrInvalid(guess, ticlist):
    try:
        for rows in ticlist:
            if guess in rows:
                return True
    except ValueError:
        print('Error')
        return False
def get_list(length):
    row = 0
    ticlist = []
    line_list = []
    while length >= 3 and row < length: 
        line_list =[]
        for x in range(length):
            x = x+1
            formula = (x)+(length*row)
            line_list.append(formula)
            if x == length:
                break
        ticlist.append(line_list)
        row += 1
    return ticlist
def playerA(ticlist):
    guess = int(input('Enter number: '))
    if validOrInvalid(guess, ticlist) is True:
        for rows in ticlist:
            for index, items in enumerate(rows):
                if guess == items:
                    rows[index] ='X'
                    return ticlist
def playerB(ticlist):
    guess = int(input('Enter number: '))
    if validOrInvalid(guess, ticlist):
        for rows in ticlist:
            for index, items in enumerate(rows):
                if guess == items:
                    rows[index] ='O'
                    return ticlist  
def victory(ticlist, length):
    for lines in ticlist:
        print(lines)
        print(ticlist)

length = int(input('Input demension of the board:'))
ticlist = get_list(length)
print(ticlist)
player_one = playerA(ticlist)
for index, rows in enumerate(ticlist):
    print(ticlist[index])
player_two = playerB(ticlist)
for index, rows in enumerate(ticlist):
    print(ticlist[index])
print('#################')