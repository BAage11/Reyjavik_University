# Given a string named s, move the first 3 letters to the back of the string.
# Print it.
 
# For example, given s = "magic tortoise"
# the output will be
# ic tortoisemag

s = input("Input a string: ")

s = s[3:] + s[0:3]

print(s)