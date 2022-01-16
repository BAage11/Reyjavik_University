# Create a program that takes 3 integers as input and prints the integer with the lowest value. 

num1 = int(input("Please type a number: "))
num2 = int(input("Please type another number: "))
num3 = int(input("Please type the third number: "))

if num1 < num2 and num1 < num3:
  print("The lowest value is:", num1)
elif num2 < num1 and num2 < num3:
  print("The lowest value is:", num2)
else:
  print("The lowest value is:", num3)
