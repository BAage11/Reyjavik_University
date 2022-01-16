# Create a program that takes 2 strings as input. If the strings are the same length the program should print “The strings are the same length”. If they are not the same length the program shouldn’t print anything. 
 

str1 = input("Please type a name: ")
str2 = input("Please type another name: ")
 
len1 = len(str1)
len2 = len(str2)

if len1 == len2:
  print("The strings are the same length")
