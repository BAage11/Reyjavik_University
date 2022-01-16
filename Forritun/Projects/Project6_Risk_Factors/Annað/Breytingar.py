
def read_file(file_):
  """ Lesa inn skrá sem notandi vill opna og ná í textann úr skránni. Ef skrá fyrirfinnst ekki, er prentuð villuskilaboð. """
  try:
    files = open(file_, "r")
  except:
    print("Cannot find file ", files)
    quit() 
  text_in_file = []
  for text in files:
    text = text.strip()
    text_in_file += text.split("\n")
  return text_in_file    

def header():
  """ Prentar út fyrirsögn fyrir niðurstöður úr skrá. """
  print("{:<29s}{:<29s}{:<29s}".format("Indicator", "Min", "Max"))
  print("-" * 87)


file_input = input("Enter filename containing csv data:")
read_file_ = read_file(file_input)

#Heart disease Death Rate = 1
#Motor vehicle Death Rate = 5
#Teen birth rate = 7
#Adult smoking = 11
# Adult obesity = 13


def sentence_list(text_in_file):
  sentences = []
  for string in text_in_file:
    string = string.strip()
    sentence = string.split(",")
    
    print(list(sentences[0])+list(sentences[1])+list(sentences[5])+list(sentences[7])+list(sentences[11])+list(sentences[13]))
    try:
      all_data.append(list(sentence[0])+list(sentences[1])+list(sentences[5])+list(sentences[7])+list(sentences[11])+list(sentences[13]))

      #sentence.append(sentences)
    except:
      print(sentence,"Villa")
#all_data.append(sentences[1]+sentences[5]+sentences[7]+sentences[11]+sentences[13])
#  print(all_data)

all_data=[]
#header()
sentence_list(read_file_)
print(all_data)