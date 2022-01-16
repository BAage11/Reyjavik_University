import string
import operator

def get_words(filename):
    file = open (filename, 'r')
    words = ''
    for letters in file:
        words += letters
    file.close()
    return words

def get_rid_of_punct(words):
    newlist = []
    for word in words:
        newlist.append(word.strip(string.punctuation))
    return newlist

def get_list(words):
    words = words.lower()
    words = words.split()
    return words

def previous_word(word_list):
    bigram_dict = {}
    previous_word = ""
    for word in word_list:
        if previous_word != "":
            build_word = (previous_word, word)
            previous_word = word
            if build_word in bigram_dict:
                bigram_dict[build_word] += 1
            else:
                bigram_dict[build_word] = 1
        else:
            previous_word = word
    return bigram_dict


#main
filename = input('Enter name of file: ')
words_str = get_words(filename)
word_list = get_list(words_str)
word_list = get_rid_of_punct(word_list)
bigram = previous_word(word_list)
items = bigram.items()              # all the key-value pairs as a list of tuples (bls. 459)
s = sorted(items, key = operator.itemgetter(1), reverse=True)
first_ten = (s[0:10])
print(first_ten)