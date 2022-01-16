word = input("Enter a word: ")   
new_word = ""
length = len(word)

for index in range(int(length)):       
  if word[index] in ['a','e','i','o','u']:
    for pos in range(index, int(length)):                       
      if(index < length - 1):
        new_word = new _word + word[pos]
                     
# Find the sub word without starts with vowel
for index in range(int(length)):
  if word[index] in ['a','e','i','o','u']:
    break
  else:
    new_word = new_word + word[index]
  
  # Print the word which is Pig Latin equivalent
  print(new_wo + "ay")

# Call main method
# main()