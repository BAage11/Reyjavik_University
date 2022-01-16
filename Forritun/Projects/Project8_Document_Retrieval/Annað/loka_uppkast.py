import string


def GetFile(filename):
  """ Athugar hvort að skrá sé til. Ef skrá er til, þá er búinn til textastrengur með orðum í skrám. Ef skrá finnst ekki, prentast villuskilaboð. """
  try:
    file_str = ""
    file_list = []
    file = open(filename, "r")
    for letters in file:
      if "<NEW DOCUMENT>" not in letters:
        file_str += letters.lower()
      if "<NEW DOCUMENT>" in letters:
        file_list.append(file_str)
        file_str = ""
    file_list.append(file_str)
    file_list.pop(0)
    file.close()
    return file_list
  except FileNotFoundError:
    return False

def GetWordInLine(line_list):
  file_line_list = []
  for lines in line_list:
    words = lines.split()
    file_line_list.append(words)
  return file_line_list


def GetRidOfPunct(word_list):
  """ Lagar til textaskrá, tekur út greinarmerki, settur orð sem lágstafi (svo leit eftir hástöfum og lágstöfum leiðir að sömu niðurstöðu) og tekur út línubil. """
  whole_nested_words = []
  print(word_list)
  for words in word_list:
    nested_words = []
    for word in words:
      word = word.strip(string.punctuation)
      nested_words.append(word)
    whole_nested_words.append(nested_words)
  print(whole_nested_words)
  return whole_nested_words

# def StrToList(file_str):
#   """ Býr til lista úr textastreng, aðgreint með kaflaskiptingar í textaskrá ("New # document"). Tekur að lokum út kaflaheiti. """
#   file_list = file_str.split('new document')
#   file_list.pop(0)
#   return file_list

def CreateDict(word_list):
  the_dict = {}
  for index, words in enumerate(word_list):
    for word in words:
      if word in the_dict:
        the_dict[word].append(index)
      if word not in the_dict:
        the_dict[word] = [index]
  print(the_dict)
  return the_dict

def TrueChoices(choices):
  """ Val notanda hvaða aðgerð hann/hún vill framkvæma. """
  if choices == 1 or choices == 2:
    return True
  else:
    print("Exiting program.")
    return False

def PrintOptions():
  """ Prentað út skilaboð til notanda um mögulegar aðgerðir. """
  print("1. Search Documents")
  print("2. Print Documents")
  print("3. Quit Program")

def SearchDocs(file_list):
  counter = 1
  file_dir = {}
  for items in file_list:
    file_dir[items] = counter
    counter += 1
  if len(file_dir) == 0:
    print("No match.")
  else:
    return file_dir

# def getKeysByValue(file_dir, doc_print):
#   listOfKeys = []
#   listOfItems = file_dir.items()
#   for item in listOfItems:
#     if item[1] == doc_print:
#       listOfKeys.append(item[0])
#   return listOfKeys

# Main program starts here:
filename = input('Document collection: ')
file_str = GetFile(filename)
words = GetWordInLine(file_str)
if GetFile(filename) == False:
  print("Documents not found.")
  quit()

choices = 1
file_punct = GetRidOfPunct(words)
# file_list = StrToList(file_punct)
dictionary = CreateDict(file_punct)

while TrueChoices(choices) == True:
  PrintOptions()
  choices = int(input("> "))
  if choices == 1:
    search_words = input("Enter search words: ").split()
    results = set()
    for key in search_words:
      if results != set():
        results = results.intersection(set(dictionary[key]))
      if results == set():
        results = set(dictionary[key])
    empt = ""
    for item in file_dir.values():
      empt += str(item) + " "
    print(empt)
  elif choices == 2:
    print_doc = input("Enter document number: ")
    print(file_str[int(print_doc)])
    # word_key_document = getKeysByValue(file_list, print_doc)
    # print(word_key_document)
