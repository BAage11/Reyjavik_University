# Range test
# Write a function that takes an integer as an argument and returns True if the number is within the range 1 to 555 (not inclusive, i.e. neither 1 nor 555 are in range).
# Also write a statement that calls the function with the given input as an argument.

def number_range(number):
  if 1 < number < 555:
    return True
  else:
    return False

num = int(input("Enter a number: "))
if number_range(num):
  print(num, "is in range.")
else:
  print(num, "is outside the range!")
