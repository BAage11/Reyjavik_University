import string

vowels = 'aeiou'
word = input("Enter a word: ")

while word != '.':
  first_letter = word[:1]
  if first_letter in vowels:  # word begins with a vowel
    pig_word = word + "yay"
  else:                       # word starts with a consonant
    pig_word = word
    for index, letter in enumerate(word):
      if letter in vowels:
        consonants = word[:index]
        rest = word[index:]
        pig_word = rest + consonants
        break
    pig_word = pig_word + "ay"

  print(pig_word)
  word = input("Enter a word: ")