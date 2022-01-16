# Create a program that takes an integer as input, let´s call it turns. This integer should indicate how many times the user wants to input a new integer. Next the program should let the user input turns many integers. The program should then print the sum of all the negative integers the user input. 

turns = int(input("How many numbers would you like to type? "))
counter = 0
sum_negative = 0

while counter != turns:
  number = int(input("Please type a number: "))
  if number < 0:
    sum_negative += number

  counter += 1

print("The sum of negative numbers are:", sum_negative)
