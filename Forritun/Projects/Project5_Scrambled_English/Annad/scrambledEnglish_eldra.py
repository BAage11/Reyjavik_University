import random
import string

def get_word_string(filename):
  """ Lesa inn skrá notanda. Ef skráarheiti fyrirfinnst ekki, prentast villuskilaboð. """
  try:
    file = open(filename, "r")
    read_file = file.read()
    file.close()
    return read_file
  except:
    return("File " + filename + " not found")
  

def scramble_string(word_string):
  """ Skipta orðum (words) milli bila (" "). Býr svo til nýjan lista sem tekur stafina (að undanskildum byrjunar- og endastaf) og ruglar þeim. Orð er svo samansett aftur undir heitinu "word_list". """
  try:
    word_list = []
    words = word_string.split(" ")
    for word in words:
      whole_word = list(word)

      if len(word) < 4:
        word_list.append("".join(whole_word))
      elif len(word) >= 4:
        middle_text = whole_word[1:-1]
        random.shuffle(middle_text)
        word_list.append(whole_word[0] + "".join(middle_text) + whole_word[-1])
        
    return " ".join(word_list)
  
  except:
    whole_word = ""
    return whole_word




random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)

scrambled_string = scramble_string(word_string)
print(scrambled_string)
