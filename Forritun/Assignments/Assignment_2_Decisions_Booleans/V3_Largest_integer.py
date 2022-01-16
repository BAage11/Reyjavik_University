# Write a program that reads in 3 integers and prints out the maximum of the three.

num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

if num1 >= num2 and num1 >= num3:
    print("The maximum is: ", num1)

elif num2 >= num1 and num2 >= num3:
    print("The maximum is: ", num2)

else:
    print("The maximum is: ", num3)
