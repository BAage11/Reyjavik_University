def the_range(x):
    if 1 <= x <= 10:
        return True
    else:
        return False

def moves(x, y):
    if x == "r" and y < 10:
        y += 1
    elif x == "r" and y == 10:
        y += 0
    
    if x == "l" and y > 1:
        y -= 1
    elif x == "l" and y == 1:
        y += 0
    return y
    return True
    
    if x != "l" or x != "r":
        return False

     
def valid_inputs(x):
    if x == "r" or x == "l":
        return True
    else:
        return False

def text_one():
    return "l - for moving left"

def text_two():
    return "r - for moving right"

def text_three():
    return "Any other letter for quitting"

def text_four():
    return "New position is:"

def choice_input():
    return input("Input your choice: ")

def position_input():
    return int(input('Input a position between 1 and 10: '))



position = position_input()

while the_range(position) == True:
    print(text_one())
    print(text_two())
    print(text_three())
    choice = choice_input()

    if valid_inputs(choice) == True:
        position = moves(choice, position)
        print(text_four(),position)
    
    if valid_inputs(choice) == False:
        break