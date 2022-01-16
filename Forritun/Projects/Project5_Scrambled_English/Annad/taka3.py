# Write a Python program for the Scrambled English project on page 422 in the textbook.

import random
import string

def get_word_string(filename):
  try:
    file = open(filename, "r")
    return file
  except:
    print("File X not found")

def scramble_string(word_string):
  new_list = []
  for word in word_string:
    j = word.split(" ")
    new_list.append(j)

  return new_list


  # foo = list(word_string[1:-1])
  # random.shuffle(foo)
  
  # return word_string[0] + ''.join(foo) + word_string[-1]


random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)

filename.close()