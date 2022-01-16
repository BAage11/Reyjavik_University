# Write a Python program that allows the user to perform three operations on a dictionary:
# add_to_dict(): takes a dictionary, a key, a value and adds the key,value pair to the dictionary. If key is already in dictionary then it displays the error message: "Error. Key already exists.". 
# remove_from_dict(): takes a dictionary and key and removes the key from the dictionary.  If no such key is found in the dictionary then it prints: "No such key exists in the dictionary."
# find_key(): takes dictionary and key and prints the value corresponding to the key from the dictionary: print("Value: ", value). If key is not found, then prints: "Key not found." 

# The user is presented with a menu and repeatedly offered to perform an operation until he/she quits. Finally, a list of the key-value pairs in the dictionary is printed out.

def menu_selection():
  print("Menu: ")
  choice = input("add(a), remove(r), find(f): ")
  return choice

def execute_selection(choice, a_dict):
  if choice == "a":           # add to dictionary
    key = input("Key: ")
    value = input("Value: ")
    if key in a_dict:
      print("Error. Key already exists.")
    else:
      a_dict[key] = value
  elif choice == "r":         # remove from dictionary
    remove_key = input("key to remove: ")
    if remove_key in a_dict:
        key_removed = a_dict.pop(remove_key)
        return key_removed
    else:
      print("No such key exists in the dictionary.")
  elif choice == "f":         # find in dictionary
    try:
      key = input("Key to locate: ")
      print("Value:", a_dict[key])
    except KeyError:
      print("Key not found.")

def dict_to_tuples(a_dict):
  dict_list = []
  for key,value in a_dict.items():
    temp = (key, value)
    dict_list.append(temp)
  return dict_list  

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()