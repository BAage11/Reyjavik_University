# Create a program that accepts 2 integers as input and outputs the greater integer. If the integers are equal the program should print the text “the numbers are equal”. 

num1 = int(input("Please type a number: "))
num2 = int(input("Please type another number: "))

if num1 > num2:
  print(num1, "is larger")
elif num1 < num2:
  print(num2, "is larger")
elif num1 == num2:
  print("the numbers are equal")
  