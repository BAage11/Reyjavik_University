# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num0 = 0
num1 = 1
num2 = 2
sum = num0 + num1 + num2
counter = 0

if n <= 0:
  print("Not possible")
elif n == 1:
  print(n)
elif n >= 2:
  while counter < n:
    num0 = num1
    num1 = num2
    num2 = sum
    sum = num0 + num1 + num2
    print(num0)
    counter += 1
