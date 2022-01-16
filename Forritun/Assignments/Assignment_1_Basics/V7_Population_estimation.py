# Assume that the current US population is 307,357,870 and that these rates of change are provided:
# •	a birth every 7 seconds
# •	a death every 13 seconds
# •	a new immigrant every 35 seconds
# Write a program that takes years as input (as an integer) and prints out an estimated population (as an integer).  Assume that there are exactly 365 days in a year.

years_str = input("Years: ") # do not change this line
years_int = int(years_str)

years_int *= 365 * 24 * 60 * 60 
# Breyta ár í sekúndur, líkt og forsendur sem gefnar eru upp og notaðar eru hér að neðan.

population = 307357870
population += years_int // 7
population -= years_int // 13
population += years_int // 35

print("New population after", years_str, " years is ", int(population)) # do not change this line



