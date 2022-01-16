# Exercise no. 44 in chapter 4 in the textbook.
# You should output the result in a table, formatted in the following manner:
# The first line contains the word "Upper case", right justified, 15 spaces wide, followed # by the count of upper case characters, right justified, 5 spaces wide.
# The second line contains the word "Lower case", right justified, 15 spaces wide, followed # by the count of lower case characters, right justified, 5 spaces wide.
# The third line contains the word "Digits", right justified, 15 spaces wide, followed by # the count of digits, right justified, 5 spaces wide.
# The fourth line contains the word "Punctuation", right justified, 15 spaces wide, followed # by the count of punctuation characters, right justified, 5 spaces wide.
# The input prompt should be: "Enter a sentence. "

word = str(input('Enter a sentence: '))
upper_case = 0
lower_case = 0
digits = 0
space = 0
punctuation=0

for i in word:
    if i.islower():
        lower_case+=1
    elif i.isupper():
        upper_case+=1
    elif i.isnumeric():
        digits+=1
    elif i.isspace():
        space+=1
    else :
        punctuation+=1

print('{:>15s} {:5d}'.format('Upper case',upper_case))
print('{:>15s} {:5d}'.format('Lower case',lower_case))
print('{:>15s} {:5d}'.format('Digits',digits))
print('{:>15s} {:5d}'.format('Punctuation',punctuation))
