# Blaðsíða 158 (og bls. 136) - Code Listing 2.19

# Perfect number checker
# Classify the number based on its divisor sum

# Get a number to check
number_str = input("Please enter a number to check: ")
number_int = int(number_str)

# Find and sum up the divisors
divisor = 1
sum_of_divisors = 0
while divisor < number_int:
  if number_int % divisor == 0:   # divisor evenly divides the number_int 
    sum_of_divisors = sum_of_divisors + divisor
  divisor = divisor + 1

# Classify the result
if number_int == sum_of_divisors:
  print(number_int, "is perfect")
elif number_int < sum_of_divisors:
  print(number_int, "is abundant")
else:
  print(number_int, "is deficient")
number_int += 1
