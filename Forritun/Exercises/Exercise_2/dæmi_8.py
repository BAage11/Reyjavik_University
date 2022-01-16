# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. Next you should let the user input size many values to a list. Next you should create a list that has all the same values as the initial list except with no duplicates. You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()). 
 
def list_value(list_size):
  """ Settur gildi inn í lista, sem notandi velur. """
  the_list = []
  counter = 0
  value_num = 1
  while list_size > counter:
    value = input("value no."+str(value_num)+": ")
    try:
      value = int(value)
      counter += 1
      value_num += 1      
      the_list.append(value)
    except:
      print("Not a valid number.")
  return the_list

def no_duplicates(user_list):
  """ Athugar gildi á lista og tekur út allar endurtekningar. """
  final_list = []
  for number in user_list:
    if number not in final_list:
      final_list.append(number)
  return final_list

size = int(input("Input the size of the list: "))
list_size = list_value(size)
final_list = no_duplicates(list_size)

print("The list:", [int(i) for i in list_size])
print("The list with no duplicates:", [int(i) for i in final_list])