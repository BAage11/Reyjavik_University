# Write a program that reads a file called 'test.txt' and prints out the contents on the screen after removing all spaces and newlines. Punctuations will be preserved.

# For example, if 'test.txt' contains:
# This is a test file, for chapter 06.
# This a new line in the file!
# Then, your program's output will show:
# Thisisatestfile,forchapter06.Thisanewlineinthefile!
# Hint: Consider using the strip() and replace() functions.

content = open("test.txt", "r")

for line in content:
    line = line.replace(" ", "").strip("\n")
    print(line, end="")

content.close()

# -----------------------------------------------------------------------------------------------------------
# Write a function named is_float(s) that takes one argument that is a string.  It returns True if string s represents a floating point value and returns False otherwise.  You are required to use try-except.  The basic concept is to "try" to convert string s to a float and if it succeeds, return True, but if it fails (that is, an exception is raised), return False.  Note that float() raises a  ValueError exception.


def is_float(s):
    try:
        s == float(s)
        return True
    except ValueError:
        return False


print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))

# -----------------------------------------------------------------------------------------------------------
# Write a Python program that reads a file named words.txt containing one word/token per line with an empty line between sentences.  The program prints out the longest word found in the file along with its length.

read_file = open("words.txt", "r")


def find_longest_word(read_file):
    longest_word = ""
    for word in read_file:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word is '" + longest_word.strip() +
          "' of length", len(longest_word.strip()))


find_longest_word(read_file)
read_file.close()

# -----------------------------------------------------------------------------------------------------------
# Write a function named safe_input(prompt, type) that works like the Python input function, except that it only accepts the specified type of input.  The function two arguments:

# prompt: of type string
# a_type: either the type int, float or str

# The function should keep prompting the user for input until the user inputs the correct type.  At the end the function should return the converted value.


def safe_input(prompt, type):
    while True:
        try:
            user_input = input(prompt)
            if type == str:
                user_input = str(user_input)
            elif type == int:
                user_input = int(user_input)
            else:
                user_input = float(user_input)
            return user_input

        except ValueError:
            print("Error: please enter a value of ", type)


print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

# -----------------------------------------------------------------------------------------------------------
# Write a Python program that reads a file named words.txt containing one word/token per line with an empty line between sentences and writes out one sentence per line into a file called sentences.txt. The program should also print out (to the screen) each sentence.

# It is ok to have one space between the end of a sentence (e.g. period) and the last word.

input_file = open("words2.txt", "r")
output_file = open("sentences.txt", "w")
new_str = ""

for word in input_file:
    if word != "\n":
        word = word.strip()
        if word == ".":
            new_str += word + " \n"
        else:
            new_str += word + " "

print(new_str, end="")

input_file.close()
output_file.close()
