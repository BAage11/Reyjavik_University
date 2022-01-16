# Write a Python program using for loops that, given an integer n, prints all the perfect numbers from 1 to n.
# A perfect number is an integer whose sum of integer divisiors (excluding the number itself) add up to the number.
# For example, 6 is a perfect number because the sum of its integer divisors (1+2+3) is equal to 6.

top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1, top_num):
    summa = 0
    for j in range(1, i):
        if i % j == 0:
            summa += j
      
    if summa == i:
        print(i)


