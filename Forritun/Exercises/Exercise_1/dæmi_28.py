# Create a program that takes an integer as input, let´s call it turns. This integer should indicate how many times the user wants to input a new integer. Next the program should let the user input turns many integers. The program should then print how many negative integers the user input and how many positive integers the user input. 

turns = int(input("How many times would you like to type a number? "))
counter = 0
negative_numbers = 0
positive_numbers = 0

while counter != turns:
  number = int(input("Please type in a number:"))

  if number < 0:
    negative_numbers += 1
  if number >= 0:
    positive_numbers += 1
  
  counter += 1

print("The number of negative numbers typed:", negative_numbers)
print("The number of positive numbers typed:", positive_numbers)
