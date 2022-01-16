# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. Next you should let the user input size many values to a list. Next you should print the content of the list. 
 
def check_int(check_input):
  """ Athugar hvort að notandi hafi slegið inn tölu. Ef ekki, prentast villuskilaboð. """
  try:
    val = int(check_input)
    return val
  except ValueError:
    return print("The value typed is NOT an integer.")
  

def list_size(size_check):
  """ Leyfir notanda að slá inn tölur til að geyma í lista, út frá stærð listans sem notandi valdi. """
  final_list = []
  counter = 0
  while counter < size_check:
    value_input = input("Type a number to the list: ")
    counter += 1
    final_list.append(value_input)
  return final_list

size = input("Please type an integer (the size of the list): ")
size_check = check_int(size)
final_list = list_size(size_check)

# Breytir lista sem er allur strengir, í integer lista
print([int(i) for i in final_list])