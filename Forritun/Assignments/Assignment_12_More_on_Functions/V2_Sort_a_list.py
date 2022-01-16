# Question 2: Sort a list
# Write a function 'sort_list()' that accepts a list of integers and sorts it. The function should not explicitly return this list and yet the list will be sorted when printed within main() after being passed to sort_list() as a parameter.
# Complete the main() module such that it accepts numbers from the user, until a non-digit string is entered (you could use try-except for this), and stores them in a list called 'a_list'.

def sort_list(a_list):
  sort_a_list = a_list.sort()
  return sort_a_list

def main():
  a_list = []
  number = input("First number: ")
  while number.isdigit():
    a_list.append(int(number))
    number = input("Next number: ")
        
  print(a_list)
  print(sort_list(a_list))
  print(a_list)
    
main()