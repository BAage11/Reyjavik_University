# Project 2: Pig Latin
# Project no. 3 in chapter 4 in the textbook.
# The input prompt should be "Enter a word. "

# Enter a word: dog
# ogday
# Enter a word: scratch
# atchscray

word = input("Enter a word. ")
pig = "ay"

vowels = ("a", "e", "i", "o", "u")
letter_1 = word[0]          # greina fyrsta stafinn í orðinu

if len(word) > 0:           # athuga hvort eitthvað hafi verið skrifað
  original = word.lower()   # breyta alla stafi í lower-case
  if letter_1 == vowels:
    new_word = ""
    new_word = word[1:2] + word[0] + pig
  elif letter_1 != vowels:
    new_word =""
    new_word = word[3:] + word[0:3] + pig

else:
  print("Invalid error")    # ef ekkert er skrifað, koma upp villuskilaboð

# new_word = word + letter_1 + pig
# new_word = new_word[1:]
print(new_word)