# Create a program that takes 2 integers as input, let’s call them low and high. Your program should print all the integers between low and high (low and high included). You may assume that low is always lower than high. 

low = int(input("Please type the lower bound: "))
high = int(input("Please type the upper bound: "))

for x in range(low, high+1):
  print(x)
  
