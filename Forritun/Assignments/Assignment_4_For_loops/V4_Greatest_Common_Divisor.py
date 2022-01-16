# Write a Python program using a for loop, that given two integers as input, prints the greatest common divisor (gcd) of them.
# GCD is the largest integer that divides each of the two integers.
# For example, given the numbers 12 and 15, the output will be:
# 3

m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(1, m + 1):
  if m % i == 0 and n % i == 0:
    gcd = i

print(gcd)
