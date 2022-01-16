import random
import string

def get_word_string(filename):
    ''' Reads lines of text from filename and returns a string containing all the lines '''
    try:
        word_string = ''
        data_file = open(filename, "r")
        for line in data_file:
            word_string += line
        data_file.close()
    except FileNotFoundError:
        print("File {} not found".format(filename))
        # lika hægt að gera eftirfarandi:  print(f"File {filename} not found")
    return word_string

def scramble_word(word):
    ''' Returns a scrambled version of the word '''
    punctuation_char = ''
    character_list = list(word)
    first_char = character_list[0]

    if (character_list[-1] in string.punctuation):
        character_list_without_first_last = character_list[1:-2]
        last_char = character_list[-2]
        punctuation_char = character_list[-1]
    else:
        last_char = character_list[-1]
        character_list_without_first_last = character_list[1:-1]
    
    random.shuffle(character_list_without_first_last)
    scrambled_word = ''.join(character_list_without_first_last)
    scrambled_word = first_char + scrambled_word + last_char + punctuation_char

    return scrambled_word

def scramble_string(word_string):
    ''' Returns a scrambled version of the string of words '''
    word_string = word_string.strip()   # Strip whitespace
    list_of_words = word_string.split() # Get a list of the individual words

    scrambled_string = ''
    for word in list_of_words:
        if len(word) <= 3:
            scrambled_string += word + ' '
        else:
            scrambled_word = scramble_word(word)
            scrambled_string += scrambled_word + ' '
    return scrambled_string

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
