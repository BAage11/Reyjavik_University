import string

def GetFile(filename):
  """ Athugar hvort að skrá sé til. Ef skrá er til, þá er búinn til textastrengur með orðum í skrám. Ef skrá finnst ekki, prentast villuskilaboð. """
  try:
    file_str = ""
    file = open(filename, "r")
    for letters in file:
      file_str += letters
    file.close()
    return file_str
  except FileNotFoundError:
    return False

def GetRidOfPunct(file_str):
  """ Lagar til textaskrá, tekur út greinarmerki, settur orð sem lágstafi (svo leit eftir hástöfum og lágstöfum leiðir að sömu niðurstöðu) og tekur út línubil. """
  file_str = file_str.replace('\n', ' ')
  word_str = ""
  for letters in file_str:
    word_str += letters.strip(string.punctuation)
  return word_str.lower()

def StrToList(file_str):
  """ Býr til lista úr textastreng, aðgreint með kaflaskiptingar í textaskrá ("New document"). Tekur að lokum út kaflaheiti. """
  file_list = file_str.split('new document')
  file_list.pop(0)
  return file_list

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

def SearchDocs(file_list, search_words):
  counter = 0
  file_dir = {}
  value_list = []
  search_words = search_words.split()
  for words in search_words:
    value_list =[]
    counter = 0
    for items in file_list:
      if counter >= len(file_list):
        break
      if words in file_list[counter]:
        value_list.append(counter+1) 
      counter+=1
    file_dir[words] = value_list
  if len(file_dir) == 0:
    print("No match.")
  else:
    return file_dir

# Main program starts here:
filename = input('Document collection: ')
file_str = GetFile(filename)
if GetFile(filename) == False:
  print("Documents not found.")
  quit()

choices = 1
file_punct = GetRidOfPunct(file_str)
file_list = StrToList(file_punct)

while TrueChoices(choices) == True:
  PrintOptions()
  choices = int(input("> "))
  if choices == 1:
    search_words = input("Enter search words: ")
    file_dir = SearchDocs(file_list, search_words)
    print(file_dir)
    for key, value in file_dir.items():
      print(value)
  elif choices == 2:
    print_doc = ("Enter document number: ")

  