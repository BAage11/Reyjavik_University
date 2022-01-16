# Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.

number_int = int(input("Input a number: "))
# Búa til lista sem heldur útanum allar jákvæðar tölur sem slegnar eru inn.
max_int = [number_int]

# Check if the number typed is a positive number
while number_int >= 0:
  number_int = int(input("Input a number: "))
  # Add the typed number to the list of positive numbers
  max_int.append(number_int)
 
  # If the number is negative, stop the program
  if number_int < 0:
    print("The maximum is",max(max_int))
