# Blaðsíða 466-469 - Code listing 9.2-9.5

def add_word(word, word_count_dict):
  """ Update the word frequency: word is the key, frequency is the value. """
  if word in word_count_dict:
    word_count_dict[word] += 1
  else:
    word_count_dict = 1

import string
def process_line(line, word_count_dict):
  """ Process the line to get lowercase words to add to the dictionary. """
  line = line.strip()
  word_list = line.split()
  for word in word_list:
    # ignore the '--' that is in the file
    if word != '--':
      word = word.lower()
      word = word.strip()
      # get commas, periods and other punctuation out as well
      word = word.strip(string.punctuation)
      add_word(word, word_count_dict)

def pretty_print(word_count_dict):
  """ Print nicely from highest to lowest frequency. """
  # create a list of tuples, (value, key)
  # value_key_list = [(val, key) for key, val in d.items()]
  value_key_list = []
  for key, val in word_count_dict.items():
    value_key_list.append((val, key))
  # sort methor sorts on list's first element, the frequency.
  # reverse to get biggest first
  value_key_list.sort(reverse=True)
  # value_key_list = sorted([v,k) for k,v in value_key_list.items()], reverse=True)
  print("{:11s}{:11s}".format("Word", "Count"))
  print("_"*21)
  for val, key in value_key_list:
    print("{:12s}  {:<3d}".format(key,val))

def main():
  word_count_dict = {}
  gba_file = open("gettysburg.txt", "r")
  for line in gba_file:
    process_line(line, word_count_dict)
  print("Length of the dictionary:",len(word_count_dict))
  pretty_print(word_count_dict)

main()