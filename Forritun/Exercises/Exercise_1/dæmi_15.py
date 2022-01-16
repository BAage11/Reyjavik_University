# Create a program that lets the user input a single integer, lets call it multiplier. Next your program should print all the integers between 2 and 15 (2 and 15 included) multiplied by the value of multiplier

multiplier = int(input("Please type an integer: "))

for x in range(2, 16):
  print(x * multiplier)

