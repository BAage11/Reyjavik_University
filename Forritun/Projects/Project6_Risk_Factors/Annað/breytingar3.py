def read_file(the_file):
  """ Lesa inn skrá sem notandi vill opna og ná í textann úr skránni. Ef skrá fyrirfinnst ekki, er prentuð villuskilaboð. """
  try:
    file = open(the_file, "r")
  except:
    print("Cannot find file ", file)
    quit() 
  text_in_file = []
  for text in file:
    text = text.strip()
    text_in_file += text.split("\n")
  file.close()
  return text_in_file    

def header():
  """ Prentar út fyrirsögn fyrir niðurstöður úr skrá. """
  print("{:<29s}{:<29s}{:<29s}".format("Indicator", "Min", "Max"))
  print("-" * 87)

def sentence_list(text_in_file):
  """ Tekur heildarlista (text_in_file) og skiptir honum í nested lists út frá kommu. """
  sentence_list = []
  for string in text_in_file:
    string = string.strip()
    sentence = string.split(",")
    sentence_list.append(sentence)
  return sentence_list


file_input = input("Enter filename containing csv data: ")
open_file = read_file(file_input)
sentence_list = sentence_list(open_file)

header()

min_value_heart = ""
max_value_heart = ""
for i in sentence_list[1]:
  for j in i:
    if j < i:
      min_value_heart = i
    if j > i:
      max_value_heart = j

min_value_motor = ""
max_value_motor = ""
for i in sentence_list[5]:
  for j in i:
    if j < i:
      min_value_motor = i
    if j > i:
      max_value_motor = j

min_value_teen = ""
max_value_teen = ""
for i in sentence_list[7]:
  for j in i:
    if j < i:
      min_value_teen = i
    if j > i:
      max_value_teen = j

min_value_smoking = ""
max_value_smoking = ""
for i in sentence_list[11]:
  for j in i:
    if j < i:
      min_value_smoking = i
    if j > i:
      max_value_smoking = j 

min_value_obesity = ""
max_value_obesity = ""
for i in sentence_list[13]:
  for j in i:
    if j < i:
      min_value_obesity = i
    if j > i:
      max_value_obesity = j


print("{:<33s}{:<21s}{:>6s}      {:<15s}{:>6s}".format("Heart Disease Death Rate (2007):", "Minnesota", min_value_heart, "Mississippi", max_value_heart))
print("{:<33s}{:<21s}{:>6s}      {:<15s}{:>6s}".format("Motor Vehicle Death Rate (2009):", "District of Columbia", min_value_motor, "Wyoming", max_value_motor))
print("{:<33s}{:<21s}{:>6s}      {:<15s}{:>6s}".format("Teen Birth Rate (2009):", "New Hampshire", min_value_teen, "Mississippi", max_value_teen))
print("{:<33s}{:<21s}{:>6s}      {:<15s}{:>6s}".format("Adult Smoking (2010):", "Utah", min_value_smoking, "West Virginia", max_value_smoking))
print("{:<33s}{:<21s}{:>6s}      {:<15s}{:>6s}".format("Adult Obesity (2010):", "Colorado", min_value_obesity, "Mississippi", max_value_obesity))

# Heart disease Death Rate = 1
# Motor vehicle Death Rate = 5
# Teen birth rate = 7
# Adult smoking = 11
# Adult obesity = 13
