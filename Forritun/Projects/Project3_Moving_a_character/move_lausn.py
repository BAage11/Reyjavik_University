
MAX = 10
MIN = 1

def readPosition():
    pos = int(input("Input a position between " + str(MIN) + " and " + str(MAX) + ": "))
    return pos

def displayMenu():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def readChoice():
    choice = input("Input your choice: ")
    return choice

def newPosition(pos, choice):
    if choice == 'l':
        if pos > MIN:
            pos -= 1
    elif choice == 'r':
        if pos < MAX:
            pos += 1
    return pos

# The main program starts here
choice = 'l'
pos = readPosition()

while choice == 'l' or choice == 'r':
    displayMenu()
    choice = readChoice()
    pos = newPosition(pos, choice)
    print("New position is:", pos)