# Find minimum
# Write a function named find_min that takes two numbers as arguments and returns the minimum of the two.
# Also write a statement that calls the function using the given input as arguments.

# find_min function definition goes here
def find_min(num1, num2):
  if num1 > num2:
    number = num2
  elif num1 < num2:
    number = num1
  else:
    number = num1

  return number

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
minimum = find_min(first, second)


print("Minimum: ", minimum)