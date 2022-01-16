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
    print("File " + filename + " not found")


def scramble_string(word_string):
  """ Skipta orðum (words) milli bila (" "). Býr svo til nýjan lista sem tekur stafina (að undanskildum byrjunar- og endastaf)og ruglar þeim. Orð er svo samansett aftur undir heitinu "word_list". """
  word_list = []
  words = word_string.split(" ")
  for word in words:
    if len(word) < 4:
      word == word
      word_list.append(word)
    elif:
        middle_text = whole_word[1:-1]
        random.shuffle(middle_text)
        word_list.append(whole_word[0] + "".join(middle_text) + whole_word[-1])
    else:
      whole_word = list(word)
    
    if whole_word[-1] is ',' or '.':
      if ',' is whole_word[-1]:
        whole_word.pop()
        middle_text = whole_word[1:-1]
        random.shuffle(middle_text)
        word_list.append(whole_word[0]+ "".join(middle_text) + whole_word[-1] + ',')
      if '.' is whole_word[-1]:
        whole_word.pop()
        middle_text = whole_word[1:-1]
        random.shuffle(middle_text)
        word_list.append(whole_word[0]+ "".join(middle_text) + whole_word[-1] + '.')
        
  return " ".join(word_list)


random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
