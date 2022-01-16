# Create a program that takes 2 integers as input, let’s call them low and high. Your program should print the sum of all the odd numbers between low and high(low and high included). You may assume that low is always lower than high.

low = int(input("Please type in the lower bound: "))
high = int(input("Please type in the higher bound: "))
sum = 0

for x in range(low, high+1):
  if x % 2 == 1:
    sum += x

print("The sum of odd numbers between low and high is:", sum)