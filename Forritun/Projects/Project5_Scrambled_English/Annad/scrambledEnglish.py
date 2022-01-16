# Write a Python program for the Scrambled English project on page 422 in the textbook.

import random
import string

def get_word_string(filename):
  try:
    file = open(filename, "r")
    return file
  except:
    print("File", filename, "not found")

def scramble_string(word_string):
  scrambled_string = []
  
  for word in word_string:
    scrambled_string += word.split(" ").extend()
  
  return scrambled_string

random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)