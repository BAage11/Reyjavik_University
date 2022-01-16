# Write a program that asks for name from the user and then asks for a number and stores the two in a dictionary as key-value pair.
# The program then asks if the user wants to enter more data (More data (y/n)? ) and depending on user choice, either asks for another name-number pair or exits and stores the dictionary key, values in a list of tuples and prints a sorted version of the list.
# Note: Ignore the case where the name is already in the dictionary. 
 
def enter_data(a_dict):
  name = input("Name: ")          # Key
  number = input("Number: ")      # Value
  a_dict[name] = number

def dict_to_tuples(dictionary):
  dict_list = []
  for key,value in dictionary.items():
    temp = (key, value)
    dict_list.append(temp)
  return dict_list

a_dict = {}
choice = "y"
while choice == "y":
  enter_data(a_dict)  
  choice = input("More data (y/n)? ")

dict_list = dict_to_tuples(a_dict)
print(sorted(dict_list))


# def enter_data(a_dict):
#   name = input("Name: ")
#   number = input("Number: ")
#   a_dict[name] = number

# def more_data():
#   more = input("More data (y/n): ")
#   return more.lower() == "y"
# 
#   def dict_to_tuples(the_dict):
#     dict_list = []
#     for key,value in the_dict.items:
#       temp = (key, value)
#       dict_list.append(temp)
#     return dict_list

# the_dict = {}
# go_again = True
# while go_again:
#   enter_data(the_dict)
#   go_again = more_data()

# dict_list = dict_to_tuples(the_dict)
# print(sorted(dict_list))