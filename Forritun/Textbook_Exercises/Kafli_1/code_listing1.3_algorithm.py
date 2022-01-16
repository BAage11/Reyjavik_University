# Blaðsíða 102-105  -  Code Listing 1.3

# Calculate rainfall in gallons for some number of inches on 1 acre
# 1. Prompt the user for the number of inches that has fallen
# 2. Find the volume (in cubic feet) of water (where volume = depth * area)
# 3. Convert the volume (in cubic feet) to gallons

inches_str = input("How many inches of rain have fallen? ")
inches_float = float(inches_str)

# 1 acre = 43,560 square feet
volume = (inches_float / 12) * 43560

# 1 cubic foot = 7.48051945 gallons
gallons = volume * 7.48051945

print(inches_float, "in. rain on 1 acre is", gallons, "gallons")

