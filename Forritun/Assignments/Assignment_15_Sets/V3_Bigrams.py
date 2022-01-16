# Write a program that reads in a file and prints out the 10 most frequent bigrams in the file. A bigram is a sequence of two adjacent words.
# Note that you should use a dictionary (not a set) in this project, because you need to keep track of the counts of each bigram (thus a key-value pair).
# Further instructions:
# all words need to be converted to lower case
# all words need to be stripped of punctuations
# The keys in the bigram dictionary should be tuples (word1, word2)
# The values are the occurences of the given bigram in the text
# Dictonaries are unordered collections. You can however, transform a dictionary to a list of tuples (using the items() method) and then sort it. Look at itemgetter on pages 355-356 in the textbook.

import operator
import string

def make_word_list(file):
  file_list =[]
  for line in file_open:
    line = line.strip(string.punctuation)
    list_line = line.split()
    for index in list_line:
      index_strip = index.strip(string.punctuation)
      file_list.append(index_strip)
  return file_list
  
def make_bigram(_list):
  bigram_dict = {}
  previous_word = ""
  for word in _list:
    if previous_word != "":
      build_word = previous_word + "," + word
      previous_word = word
      if build_word in bigram_dict:
        bigram_dict[build_word] += 1 
      else:
        bigram_dict[build_word] = 1
    else:
      previous_word = word
  return bigram_dict


# Main program starts here:
file = input("Enter name of file: ")
file_open = open(file, "r")
word_list = make_word_list(file_open)
bigram = make_bigram(word_list)
items = bigram.items()

high_to_low = sorted(items, key = operator.itemgetter(1), reverse=True)
top_ten = high_to_low[0:10]
print((tuple(top_ten[1][0].split(",")), bigram[top_ten[1][0]]))

print([(tuple(top_ten[i][0].split(",")), bigram[top_ten[i][0]]) for i,k in enumerate(top_ten)])
