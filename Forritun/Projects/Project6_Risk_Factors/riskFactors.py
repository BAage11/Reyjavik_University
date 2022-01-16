def read_file(the_file):
  """ Lesa inn skrá sem notandi vill opna og ná í textann úr skránni (og hreinsa til textann). Ef skrá fyrirfinnst ekki, er prentuð villuskilaboð. """
  try:
    file = open(the_file, "r")
  except:
    print("Cannot find file ", the_file)
    header()
    quit()
  text_in_file = []
  for text in file:
    text = text.strip()
    text_in_file += text.split("\n")
  file.close()
  return text_in_file    

def header():
  """ Prentar út fyrirsögn fyrir niðurstöður úr skrá. """
  print("{:<33s}{:<33s}{:<21s}".format("Indicator", "Min", "Max"))
  print("-" * 87)

def sentence_list(text_in_file):
  """ Skiptir heildarlista í viðeigandi nested lista þar sem gögn eru geymd sem þarf að notast við, svo hægt verði að ná í viðeigandi gildi (niðurstöður). """ 
  # Header 0... - State 1...0 - Heart Disease 1...1 - Motor Vehicle 1...5 - Teen Birth 1...7 - Smoking 1...11 - Obesity 1...13
  usable_list = [[],[],[],[],[],[],[]]
  for string in text_in_file:
    # Búa til textastreng úr heildarlista, svo hægt verði að setja í nested list.
    usable_string = ""
    string = string.strip()
    sentence = string.split(",")
    if not usable_list[0]:      # Ef ekkert er í index #0 í listanum, þá:
      usable_string = (sentence[1] + "," + sentence[5] + "," + sentence[7] + "," + sentence[11] + "," + sentence[13])
      usable_list[0] = usable_string.split(",") # Headers--nested list index#1
    else:
      usable_list[1].append(sentence[0])    # States (Ríki)--nested list inded#1
      usable_list[2].append(float(sentence[1]))   # Heart Disease Death Rate--nested list                                                 index#2
      usable_list[3].append(float(sentence[5]))   # Motor Vehicle Death Rate--nested list                                                  index#3
      usable_list[4].append(float(sentence[7]))   # Teen Birth Rate--nested list index#4
      usable_list[5].append(float(sentence[11][:-1]))   # Adult Smoking--nested list index#5
      usable_list[6].append(float(sentence[13][:-1]))   # Adult Obesity--nested list index#6
  return usable_list

def print_results(list_):
  for i,v in enumerate(list_[0]):
    i += 2      # i byrjar á index 0, svo það þarf að hefja það upp um tvö gildi svo það  	              byrji á index 2 í staðinn. Vilt byrja á að prenta sentence_list index 2,                þar sem index 0 eru header-ar og index 1 eru states (sem halda alltaf sömu                index). Prentar því út nested list númer 2-7.
    print("{:<33s}{:<21s}{:>6.1f}{:6s}{:<15s}{:>6.1f}".format(v+":", sentence_list[1][sentence_list[i].index(min(sentence_list[i]))], min(sentence_list[i])," ", sentence_list[1][sentence_list[i].index(max(sentence_list[i]))], max(sentence_list[i])))

# Main:
file_input = input("Enter filename containing csv data: ")
open_file = read_file(file_input)
sentence_list = sentence_list(open_file)

header()
print_results(sentence_list)