# Project 2: Pig Latin
# Project no. 3 in chapter 4 in the textbook.
# The input prompt should be "Enter a word. "

# Enter a word: dog
# ogday
# Enter a word: scratch
# atchscray

word = str(input("Enter a word: "))

vowels = 'aeuio'
first_letter = word[0]
first_vowel = 0
yay=('yay')
ay = ('ay')

if first_letter in vowels:
    print (word + yay)

elif first_letter not in vowels:
    for index, x in enumerate(word):
        if x == 'a' or x == 'e' or x == 'u' or x == 'i' or x =='o': 
            first_vowel = word[index]    #index is where the first vowel is in the word
            consonant, rest = word.split(first_vowel) #splitting by the first vowel
            print (first_vowel + rest + consonant + ay)
            break     
else:
    print('')
