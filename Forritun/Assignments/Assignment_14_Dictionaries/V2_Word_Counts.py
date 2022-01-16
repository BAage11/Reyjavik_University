# Write a program that reads a text file (you don't have to error check the filename), keeps a count of the individual words in the file using a dictionary and finally converts the dictionary to a list of tuples and prints out a sorted version of the list.  The main program is given, do not change it.
# Note that the counts are not case-sensitive, that is, 'Word' is the same as 'word' or 'wORd'. Also, note that your program should account for if a punctuation (like a comma) appears at the end of a word. 

import string

def get_word_list(fpointer):
  word_list = []
  for line in fpointer:
    line_list = (line.strip()).split()
    for word in line_list:
      word = word.lower()
      word = word.strip()
      word = word.strip(string.punctuation)
      word_list.append(word)
  return word_list

def word_list_to_counts(word_list):
  word_count_dict = {}
  for word in word_list:
    if word in word_count_dict:
      word_count_dict[word] += 1
    else:
      word_count_dict[word] = 1
  return word_count_dict

def dict_to_tuple(word_count_dict):
  dict_list = []
  for key,value in word_count_dict.items():
    temp = (key, value)
    dict_list.append(temp)
  return dict_list

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()