# Write a function named count_case that takes a string as an argument and returns the count of upper case and lower case characters in the string (in that order). 
 
# Also write a statement that calls the function with the given input as an argument.
# Your function definition goes here

def character(name):
  uppercount = 0
  lowercount = 0

  for letter in name:
    if letter.isupper():
      uppercount += 1
    elif letter.islower():
      lowercount += 1
    
  return uppercount, lowercount

user_input = input("Enter a string: ")
upper, lower = character(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)


