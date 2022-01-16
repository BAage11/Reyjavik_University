def header():
  """ Prentar út fyrirsögn fyrir niðurstöður úr skrá. """
  print("{:<29s}{:<29s}{:<29s}".format("Indicator", "Min", "Max"))
  print("-" * 87)


def read_file(file):
  """ Lesa inn skrá sem notandi vill opna og ná í textann úr skránni. Ef skrá fyrirfinnst ekki, er prentuð villuskilaboð. """
  try:
    open_file = open(file, "r")
  except:
    print("Cannot find file ", file)
    quit()  
  text_in_file = []
  for row_line in open_file:
    row_line = row_line.strip()
    text_in_file += row_line.split("\n")      
  return text_in_file


def the_data(text_in_file):
  the_data = []
  for string in text_in_file:
    string = string.strip()
    sentence = string.split(",")
    the_data.append(sentence)
  return the_data

def needed_data(the_data):
  needed_data = []
  for data in the_data:
    the_data.append(data)
  return needed_data
    

file_input = input("Enter filename containing csv data: ")
file_open = read_file(file_input)
the_data = the_data(file_open)
needed_data = needed_data(the_data)
header()
print(needed_data)
