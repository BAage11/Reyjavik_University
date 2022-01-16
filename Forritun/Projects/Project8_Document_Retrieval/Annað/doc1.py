
def open_document():
  try:
    document = input("Document collection: ")
    document_open = open(document, "r")     
    # encoding="cp1252"
    # encoding="windows-1252"
    # encoding="utf-8"
    print(document_open)
  
    document_stored = document_open
    document_open.close()
  except:
    print("Document not found.")

  return document_stored

open_document()

# def store_document(document):
#  document_list = []
#  for line in document:
#    line = line.split("<NEW DOCUMENT>")
#    document_list.append(line)
#  return document_list
#
#def print_command():
#  print("What would you like to do?")
#  print("1. Search Documents")
#  print("2. Print Document")
#  print("3. Quit Program")
#  choice = input()
#  return choice
#
#def user_choice(choice):
#  if choice == 1:
#   # Missing code 
#  if choice == 2:
#   # Missing code  
#  if choice != 1 or choice != 2:
#    print("Exiting program.")
#    quit()
#
# 
# # Main program starts here:
# document = open_document()
# document_list = store_document(document)
# choice = print_command()
# user_choice(choice)