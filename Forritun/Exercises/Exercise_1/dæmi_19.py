# Create a program that takes 2 integers as input, let’s call them low and high. Your program should output all the integers between low and high but only if the value of low is lower than the value of high. (if printed the values of low and high should be included)

low = int(input("Please type the lower bound: "))
high = int(input("Please type the upper bound: "))

while low <= high:
  print(low)
  low += 1
  