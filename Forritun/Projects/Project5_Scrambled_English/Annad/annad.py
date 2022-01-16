import random
import string

def get_word_string(filename):
  """ Lesa inn skrá notanda og taka út punkta(.) og kommur(,). """
  try:
    file = open(filename, "r")
    read_file = file.read()
    file.close()
    for line in read_file:
      word_str = line.strip(",.")
    return word_str
  except:
    print("File" + filename + "not found")


def scramble_string(word_string):
  """ Skipta orðum milli bila (" "), og athuga lengd orða. Ef orð er minna en 4 stafir, helst það óbreytt. Ef orð er akkúrat 4 stafir, víxlast stafur 2 og 3. Ef orð er lengra en 4 stafir, er búið til nýjan lista sem tekur stafina (að undanskildum byrjunar- og endastaf)og ruglar þeim. Orð er svo samansett aftur undir heitinu "scrambled" """
  
  words = word_string.split(" ")
  for word in words:
    lenght = len(words)
    if lenght < 4: 
      continue
    if lenght == 4:
      scrambled = (words[0], words[2], words[1], words[3])
    else:
      mid = list(words[1:-1])
      random.shuffle(mid)
      scrambled = (word[0], ''.join(mid), word[-1])
    # unscrambled = unscrambled.replace(word, scrambled, 1)

  return scrambled


random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
