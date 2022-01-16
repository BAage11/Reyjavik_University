# Fibonacci
# The Fibonacci sequence is: 1, 1, 2, 3, 5, 8, 13, ... 
# Write a function, fibo, to print the first N numbers of the Fibonacci sequence.  There should be one space between the elements.
# Also write a statement to call fibo.

import math

def fibo(n):
    for i in range(1, n + 1):
      print(int(((1 + math.sqrt(5))**i - (1 - math.sqrt(5))**i) / (2**i * math.sqrt(5))), end=" ")

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
fibo(n)
