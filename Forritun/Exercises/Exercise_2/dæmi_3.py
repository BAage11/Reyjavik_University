# Create a program that lets the user input an integer, lets call it size. This integer should denote the size of a list. Next you should let the user input size many values to a list. Next you should let the user input a value, lets call it target. Next you should count how often the value target occurs in the list. Next the program should print how many times the value target occurs in the list. You can solve this with built in functions but I recommend trying to solve this without using builtin functions as well (excluding .append()).

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


def check_value(check_target, final_list):
  """ Athugar hvort að talan sem notandi vill leita að, sé í listanum sem gerður var og telur hversu oft talan kemur fram í listanum. """
  counter = 0
  for i in final_list:
    if i == check_target:
      counter += 1
  return print("The value target occurs", counter, "times in the list.")


size = input("Please type an integer (the size of the list): ")
size_check = check_int(size)
final_list = list_size(size_check)

target = input("Check if an integer is in the list: ")
check_target = check_value(target, final_list)