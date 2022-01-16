import string

def GetFile(filename):
  """ Athugar hvort að skrá sé til. Ef skrá er til, þá er búinn til listi af orðum. 
  Ef skrá finnst ekki, skilar fallið 'False'. """
  try:
    file_str = ""
    file_list = []
    file = open(filename, "r")
    for letters in file:
      if "<NEW DOCUMENT>" not in letters:
        file_str += letters     
        # taka hverja línu af orðum, setja í textabreytu og setja í lágstafi
      if "<NEW DOCUMENT>" in letters:       
      # stoppar fallið og settur orð í textabreytu inn í lista.
        file_list.append(file_str)
        file_str = ""                 
        # Núllstilla textabreytu til að taka við næstu orðum
    file_list.append(file_str)       
    # bætir við síðustu orðum, eftir síðasta <New Document>
    file_list.pop(0)             
    # tekur í burtu fyrsta listann, sem er tómur textastrengur
    file.close()
    return file_list
  except:
    return False

def GetWordInLine(line_list):
  """ Tekur setningar í lista og eyðir út nýjum línum (enter). Settur svo í nýjan lista. """
  file_line_list = []
  for lines in line_list:
    words = lines.split()
    file_line_list.append(words)
  return file_line_list

def GetRidOfPunct(word_list):
  """ Lagar til textaskrá, tekur út greinarmerki. """
  whole_nested_words = []
  for words in word_list:
    nested_words = []
    for word in words:
      word = word.strip(string.punctuation)
      nested_words.append(word)
    whole_nested_words.append(nested_words)       
    # Settur aftur lista sem nested list
  return whole_nested_words

def CreateDict(word_list):
  """ Býr til dictionary úr nested list og 
  bættir við index á hverju orði sem value á key. """
  the_dict = {}
  for index, words in enumerate(word_list):
    for word in words:
      if word in the_dict:
        the_dict[word.lower()].append(index)    
        # ef orð er í dictionary, bættist við viðkomandi orð (key) það index (value) sem er á listanum (nested list númer....).
      if word not in the_dict:
        the_dict[word.lower()] = [index] 
        # ef orð er ekki til í dictionary, er viðkomandi orð sett sem key og index sett sem value.
  return the_dict

def TrueChoices(choices):
  """ Val notanda hvaða aðgerð hann/hún vill framkvæma. 
  Annar lykill en 1 eða 2, stoppar program-ið """
  if choices == 1:
    return True
  if choices == 2:
    return True
  else:
    print("Exiting program.")
    return False

def PrintOptions():
  """ Prentað út skilaboð til notanda um mögulegar aðgerðir. """
  print("\nWhat would you like to do?")
  print("1. Search Documents")
  print("2. Print Document")
  print("3. Quit Program")


# Main program starts here:
filename = input("Document collection: ")
file_str = GetFile(filename)
if GetFile(filename) == False:
  print("Documents not found.")
  quit()

words = GetWordInLine(file_str)

choices = 1
file_punct = GetRidOfPunct(words)
dictionary = CreateDict(file_punct)
result_str = ''

while TrueChoices(choices) == True:
  result_str = ''
  PrintOptions()
  choices = int(input("> "))
  if choices == 1:
    search_words = input("Enter search words: ").split()
    # ef leitað er eftir fleira en einu orði, eru orð sett í lista
    results = set()
    for key in search_words:
      if results != set():
        results = results.intersection(set(dictionary[key]))
        # ef set er ekki tómt, þá skal athuga hvort að orð sem verið er að skoða sé   meiginlegt því orði sem er í set - það er hvort orðin séu með sama key & value. 
      if results == set():
        try:
          results = set(dictionary[key])
        except:
          print("No match.")
        # ef set er tómt, skal bæta því orði (key) við listann set.
    for element in results:
      result_str += str(element)
      result_str += ' '
    print("Documents that fit search:",result_str)
  elif choices == 2:
    print_doc = input("Enter document number: ")
    print("Document #"+print_doc)
    print(file_str[int(print_doc)].strip("\n"))
    # prentar út key á því index-i úr upprunalega nested list, sem er það sama og document  sem notandi er að leita að.
