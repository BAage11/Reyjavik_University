# Write a program that prompts for a grade (a float).  A valid grade is between 0.0 and 10.0 (both inclusive).  A passing grade is between 5.0 and 10.0 (both inclusive).  The program pints out "Invalid grade!", "Passing grade!", or "Failing grade!", depending on the input.

grade = float(input("Input a grade: ")) # Do not change this line

if grade < 0.0 or grade > 10.0:
    print("Invalid grade!") # Do not change this line

elif grade >= 5.0 and grade <= 10.0:    
    print("Passing grade!") # Do not change this line

else:
    print("Failing grade!") # Do not change this line
