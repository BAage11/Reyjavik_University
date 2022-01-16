# Palindrome
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. Sentence-length palindromes may be written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?" or "No 'x' in Nixon".

# Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.
# Also write code that calls the function with the input as an argument and prints out the appropriate message.

def palindrome(sentence):
  sentence = sentence.lower()
  s = ""
  for letter in sentence:
    if letter.isalpha():
      s += letter
  if s == s[::-1]:
    return True
  else:
    return False


in_str = input("Enter a string: ")

if palindrome(in_str):
  print('"' + in_str + '"', "is a palindrome.")
else:
  print('"' + in_str + '"', "is not a palindrome.")

