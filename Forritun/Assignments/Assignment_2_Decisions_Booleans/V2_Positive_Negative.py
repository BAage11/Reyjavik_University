# Write a program that prompts for a number.  If it is a negative number, print 'Negative',it it is a positive number, print 'Positive', and if the input is 0, the print 'Zero'.

num = int(input("Input a number: ")) # Do not change this line

if num < 0:
    print("Negative") # Do not change this line

elif num > 0:
    print("Positive") # Do not change this line

else:
    print("Zero") # Do not change this line
