# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. Next you should let the user input size many values to a list. Next the program should print the average of all the values in the list. You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).

def check_input(value_check):
  try:
    val = int(value_check)
    return val
  except ValueError:
    return print("The input must be an integer.")

def final_list(final_list):
  the_list = []
  counter = 0
  while final_list > counter:
    values = int(input("Input a value to the list: "))
    counter += 1
    the_list.append(values)
  
  the_list_int = [int(i) for i in the_list]
  sum_of_list = sum(the_list_int)
  length_of_list = len(the_list_int)
  average_of_list = sum_of_list / length_of_list
  return average_of_list

size = input("What's the size of your list? ")
if_integer = check_input(size)
the_list = final_list(if_integer)
print("The average number of the list is:", the_list)