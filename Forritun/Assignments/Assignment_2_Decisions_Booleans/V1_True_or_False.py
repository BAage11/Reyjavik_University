# In Python, an empty object (0 for int, 0.0 for float, '' for string) is considered to be False; all non-empty objects are considered to be True.
# Write a program that prompts for an integer and prints out True if it is considered True,otherwise it prints False.

num = int(input("Input a number: ")) # Do not change this line

if num != 0:
    print(True) # Do not change this line

else:
    print(False) # Do not change this line   
