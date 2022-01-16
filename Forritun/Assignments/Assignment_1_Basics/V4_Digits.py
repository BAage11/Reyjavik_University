# Input a six-digit integer.
# Assign first_three (int) to be the first three digits.
# Assign last_two (int) to be the last two digits.
# Assign middle_two (int) to be the middle two digits.
# Print out the three values.
# Hint: use quotient (//) and remainder (%)
# For example, if the input is 123456
# The first three digits: 123
# The last two digits: 56
# The middle two digits: 34

x_str = input("Input x: ")
x_int = int(x_str)
# remember to convert to an int

# first_three =
first_three = x_int // 1000
# Færir kommuna fram um þrjár tölur, svo eftir eru fremstu tölur)

# last_two =
last_two = x_int % 100
# Færir komuna aftur um þrjár tölur og eftir situr afgangurinn

# middle_two =
middle_two = (x_int // 100) % 100
# Fyrst tekið í burtu öftustu tvær tölurnar (færir komuna fram) og svo tekið fremstu tvær tölurnar út – eftir situr tvær tölur í miðjunni miðað við forsendur

print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)
