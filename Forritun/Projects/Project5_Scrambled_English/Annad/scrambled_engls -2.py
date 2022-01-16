import random
import string

def get_word_string(File):
  word_string = ''
  try:
    File = open(File, 'r')
    for text in File:
        word_string+=text
    return word_string  
  except OSError:
    return print("File", filename, "not found")
      
def scramble_string(word_string):
  """ Skipta orðum (words) milli bila (" "). Býr svo til nýjan lista sem tekur stafina (að undanskildum byrjunar- og endastaf)og ruglar þeim. Orð er svo samansett aftur undir heitinu "word_list". """
  word_list = []
  words = word_string.split(" ")
  for word in words:
    whole_word = list(word)
    if len(whole_word) > 1:
      if whole_word[-1] not in ',' or ".":
        middle_text = whole_word[1:-1]
        random.shuffle(middle_text)
        word_list.append(whole_word[0] + "".join(middle_text) + whole_word[-1])
      elif whole_word[-1] in ',' or ".":
        middle_text = whole_word[1:-2]
        random.shuffle(middle_text)
        word_list.append(whole_word[0] + "".join(middle_text) + whole_word[-2] + whole_word[-1])
    elif len(whole_word) == 1:
      word_list.append("".join(whole_word))
  return " ".join(word_list)


random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
