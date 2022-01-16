def THE_RANGE(number):
  if 1 <= number <= 10:
    return True
  else:
    return False
  
  while THE_RANGE(number) == True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    choice = input("Input your choice: ")

    #if choice == "r" and number < 10:
    #    number += 1
    #elif choice == "r" and number == 10:
    #    number += 0
    #if choice == "l" and number > 1:
    #    number -= 1
    #elif choice == "l" and number == 1:
    #    number += 0
    #elif choice != "l" and choice != "r":
    #    print("New position is:", number)
    #    break
    #
    #print("New position is:",position)
    
    
position = int(input("Input a position between 1 and 10: "))
THE_RANGE(position)
