# Write a program that prompts the user for a name.  The program then splits the name into # first and last name (case insensitive).
# Then it:
# calls a function that returns a list of the common letters in first and last. The data structures used in this implementation can only be lists.
# calls a function that returns a set containing the common letters in first and last. The data structures used in this implementation can only be sets.
# prints out a sorted list version of the results from 1) and 2)

def common_letters_list(first,last):
  common = []
  for letter in first:
    if letter in last and letter not in common:
      common.append(letter)
  return common

def common_letters_set(first,last):
  set1 = set(first)
  set2 = set(last)
  return set1.intersection(set2)
  # return set1 & set2     -->   "&" er intersection fyrir sets (AND)

# Munurinn á set og list, er að set er ekki með duplicates og eru heldur ekki raðaðar í sérstakri röð (random). Listar er hægt að raða og hefur endurtekningar (það er hægt). 
# Operators á set : Union, Intersection, Difference, Symmetric_Difference, Isdisjoint, Issubset, Issuperset - Sjá dæmi um intersection hér að ofan.

# Main program starts here
name = input("Enter name: ").lower()
first,last = name.split()
common_list = common_letters_list(first,last)
common_set = common_letters_set(first,last)

print(sorted(common_list))
print(sorted(common_set))
