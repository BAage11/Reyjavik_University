# Blaðsíða 139-140 - Code listing 2.15
# Classify a range of numbers with respect to perfect, abundant or deficient

top_num_str = input("What is the upper number for the range: ")
top_num = int(top_num_str)
number = 2

while number <= top_num:
  # Sum up the divisors
  divisor = 1
  sum_of_divisors = 0
  while divisor < number:
    if number % divisor == 0:
      sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1
  
  # Classify the number based on its divisor sum
  if number == sum_of_divisors:
    print(number, "is perfect")
  if number < sum_of_divisors:
    print(number, "is abundant")
  if number > sum_of_divisors:
    print(number, "is deficient")
  number += 1
