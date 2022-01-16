
vowels = 'aeuio'
yay=('yay')
ay = ('ay')

while True:
  word = str(input("Enter a word: "))
  first_letter = word[0]
  
  if word == ".":
    quit()
  
  if first_letter in vowels:
    print(word + yay)
  
  elif first_letter not in vowels:
    for index, x in enumerate(word):
      if x == 'a' or x == 'e' or x == 'u' or x == 'i' or x =='o': 
            first_vowel = word[index]    #index is where the first vowel is in the word
            consonant, rest = word.split(first_vowel) #splitting by the first vowel
            print (first_vowel + rest + consonant + ay)
            break
  
            elif index == len(word) - 1:
                print(word + ay)   
    word = input('Enter a word: ')
