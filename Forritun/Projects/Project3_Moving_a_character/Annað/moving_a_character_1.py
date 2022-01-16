
def moving_character(num1):
  choice = str(input("Input your choice: "))
  if choice == "l" and 1 <= num1 <= 10:
    num1 -= 1
    print("New position is: ", num1)  
  elif choice == "r" and 1 <= num1 <10:
    num1 += 1
    print("New position is: ", num1)  
  else:
    print("New position is: ", num1)
    quit

position = int(input("Input a position between 1 and 10: "))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

moving_character(position)