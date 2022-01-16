# Create a program that takes an integer as input, let´s call it turns. This integer should indicate how many times the user wants to input a new integer. Next the program should let the user input turns many integers. The program should then print how many negative integers the user input, how many positive integers the user input, the sum of all the positive integers and the sum of all the negative integers the user input.

turns = int(input("Please enter the amount of numbers you would like to type: "))
counter = 0
sum_negative_integers = 0
sum_positive_integers = 0
total_negative = 0
total_positive = 0

while counter != turns:
  number = int(input("Please type a number: "))
  if number < 0:
    sum_negative_integers += 1
    total_negative += number
  if number >= 0:
    sum_positive_integers += 1
    total_positive += number

  counter += 1

print("Amount of negative integers typed:", sum_negative_integers)
print("Amount of positive integers typed:", sum_positive_integers)
print("Sum of all the negative integers:", total_negative)
print("Sum of all the positive integers:", total_positive)