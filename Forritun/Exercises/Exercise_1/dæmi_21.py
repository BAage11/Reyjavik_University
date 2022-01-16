# Create the same program as in assignment 20 with one change. Now the text “you picked <value>” where value is the number that was input should only be printed if that value is an odd number.

turns = int(input("How many times do you want to type a number? "))
counter = 0

while counter != turns:
  number = int(input("Please type a number: "))
  if number % 2 == 1:
    print("you picked", number)
  
  counter += 1
