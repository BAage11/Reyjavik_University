# Create a program that takes 2 integers as input, let’s call them low and high. Your program should print the sum of all the integers between low and high(low and high included) that are divisible by 3 or 5. You may assume that low is always lower than high. 

low = int(input("Please type in the lower bound: "))
high = int(input("Please type in the higher bound: "))
sum = 0

for x in range(low, high+1):
  if x % 3 == 0 or x % 5 == 0:
    sum += x

print("The sum of numbers divisible by 3 or 5, between low and high is:", sum)