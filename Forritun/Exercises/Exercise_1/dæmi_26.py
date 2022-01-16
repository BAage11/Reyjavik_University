# Create a program that takes an integer as input, let´s call it turns. This integer should indicate how many times the user wants to input a new integer. Next the program should let the user input turns many integers. The program should then print how many negative integers the user input. 

turns = int(input("How many times do you want to type a number? "))
counter = 0
sum = 0

while counter != turns:
  number = int(input("Please type a number: "))
  if number < 0:
    sum += 1

  counter += 1

print("The number of negative numbers typed are:", sum)
  
