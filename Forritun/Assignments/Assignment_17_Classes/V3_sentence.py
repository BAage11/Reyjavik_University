# Design a class called Sentence that has a constructor that takes a string representing the sentence as input. The class should have the following methods:
 
# get_first_word(): returns the first word as a string
# get_all_words(): returns all words in a list.
# replace(index, new_word): Changes a word at a particular index to "new_word".  For example, if sentences is "I'm going back", then replace(2, "home") results in "I'm going home".  If the index is not valid, the method does not do anything.

class Sentence():
  def __init__(self, sentence=""):
    self.sentence = sentence
  
  def get_first_word(self):
    words = self.sentence.split(" ")
    self.words = words
    return words[0]

  def get_all_words(self):
    return self.words

  def replace(self, index, new_word):
    try:
      self.words[index] = new_word
      return self.words
    except:
      pass

origin = Sentence("I'm going back")
origin.get_first_word()
print(origin.get_first_word())
origin.get_all_words()
print(origin.get_all_words())
print(origin.replace(1, "home"))

