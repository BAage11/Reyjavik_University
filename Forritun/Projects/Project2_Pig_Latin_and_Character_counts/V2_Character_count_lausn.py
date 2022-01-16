import string

upper_case = 0
lower_case = 0
digits = 0
punctuation = 0

sentence = input("Enter a sentence: ")

for index in range(len(sentence)):
  letter = sentence[index]
  if letter.isupper():
    upper_case += 1
  elif letter.islower():
    lower_case += 1
  elif letter.isdigit():
    digits += 1
  elif letter in string.punctuation:
    punctuation += 1

print("{:>15s} {:5d}".format("Upper case", upper_case))
print("{:>15s} {:5d}".format("Lower case", lower_case))
print("{:>15s} {:5d}".format("Digits", digits))
print("{:>15s} {:5d}".format("Punctuation", punctuation))
