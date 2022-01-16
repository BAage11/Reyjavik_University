# Write a Python program using a for loop that, given a integer n, prints out all the Armstrong number between 0 and n.  You can assume that the maximum is 999.
# An Armstrong number is a number that is equal to the sum of its digits when each digit is raised to the number of digits.
# For example:
# 6	is an Armstrong number because 6**1 = 6
# 153 is an Armstrong number because 1**3 + 5**3 + 3**3 = 153

top_num = int(input("Input a number between 0 and 999: "))

for x in range(top_num):
  total = 0
  for y in str(x):
    total += int(y)** len(str(x))
  if total == x:
    print(x)
