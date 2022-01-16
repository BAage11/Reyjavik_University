# Write a Python program using for loops that prints a pattern of *'s.  Given an input n for the number of *, the program prints 2*n-1 rows.  
# The first row cotains one *, the second row two *, ..., the n-th row contains n *, the nth +1 row contains n-1 *, the nth+2 rows contains n-2 *, etc.
# Example output given the input 5:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(1, stars + 1):   #rows (5 þegar notandi stimplar inn 5)
  for j in range(1, i + 1):     #colums (1-2-3-4-5 þegar notandi stimplar inn 5)
    print("*", end = "")
  print()

for m in range(stars, 0, -1):
  for n in range(1, m):
    print("*", end = "")
  print()

  