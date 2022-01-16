# Prime number
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Write a function named is_prime that takes an integer argument and returns True if the number is prime and False otherwise. (Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)

# Also write code that calls the function and prints out a message saying that the given number is a prime or not.

def is_prime(number):
  prime = True
  x = 2

  while x < number and prime == True:
    if number % x == 0:
      prime = False
      return False
    x = x + 1
  return True

num = int(input("Input an integer greater than 1: "))

if is_prime(num) == True:
  print(num, "is a prime")
else:
  print(num, "is not a prime")
