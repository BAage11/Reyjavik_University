# A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# Write a program using a while statement, that given an int as the input, prints out "Prime" if the int is a prime number, otherwise it prints "!Prime".

n = int(input("Input an int: ")) # Do not change this line
prime = True
x = 2

while x < n and prime == True:
  if n % x == 0:
    prime = False
  x = x + 1

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")