
def THE_RANGE(number, choice):
    """ The function checks if the number input entered by the user is between 1 and 10.
        If the number is not between 1 and 10, the function returns False. """
    if 1 <= number <= 10: 
        if choice == "l" or choice == "r":
            return True
        else:
            return False
    else:
        return False

def print_text():
    """ The text printed with each time the user wants to move the character to either left or right. Instructions on what to do next, if the user wants to continue (or not). """
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

position = int(input("Input a position between 1 and 10: "))
choice = "r"
minimum = 1
maximum = 10

while THE_RANGE(position, choice) == True:
    print_text()
    choice = input("Input your choice: ")
    
    if choice == "r" and position < maximum:
        position += 1
    if choice == "l" and position > minimum:
        position -= 1

    print("New position is:", position)
    
    