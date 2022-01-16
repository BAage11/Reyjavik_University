import string

DOCUMENT_MARKER = '<NEW DOCUMENT>'

def read_docs(filename):
    ''' Reads all documents into a list '''
    all_docs = []
    try:
        fp = open(filename)
        first = True
        doc = ''
        for line in fp:
            if line.startswith(DOCUMENT_MARKER):
                if not first:
                    all_docs.append(doc)
                    doc = '' # start new document
                else:
                    first = False
            else:
                doc += line
        else:
            all_docs.append(doc)
        fp.close()
    except FileNotFoundError:
        print('Documents not found.')
    return all_docs
    

def build_dict(all_docs):
    ''' Builds and returns a word dictionary for the given document list
        The value of each word is a set of the document numbers the word appears in
    '''
    word_dict = {}

    for count, doc_str in enumerate(all_docs): 
        word_list = doc_str.split()
        for word in word_list:
            word = word.strip().lower().strip(string.punctuation)
            if word:
                if word in word_dict:
                    word_dict[word].add(count)
                else:
                    word_dict[word]={count} # a set with one document number
    return word_dict

def get_document_set(word_dict,search_str):
    ''' Returns a set of documents containing all the words in the search_str ''' 
    search_list = search_str.strip().split()
    search_list = [word.lower() for word in search_list]
    document_set = set()

    if search_list:
        first_word = search_list[0]
        if first_word in word_dict:
            document_set = word_dict[first_word]
            # There might be more words in the search string
            if len(search_list) > 1:
                for word in search_list[1:]:
                    if word in word_dict:
                        document_set = document_set & word_dict[word]
                    else:
                        document_set = set()
                        break
    return document_set


def get_action():
    ''' Reads the action as an integer from the user. If an error occurs, returns 3 '''
    
    def print_menu():
        print("What would you like to do?")
        print("1. Search Documents")
        print("2. Print Document")
        print("3. Quit Program")
    
    print_menu()
    action = input("> ")
    return action

def action_search_words(word_dict):
    ''' Allows the user to search for a word and prints out the document numbers
        in which the words occur
    '''    
    search_str = input("Enter search words: ")
    document_set = get_document_set(word_dict,search_str)
    if document_set:
        print("Documents that fit search:",end = ' ')
        for i in document_set:
            print(i, end = ' ')
        else:
            print("\n")
    else:
        print("No match.\n")

def action_print_document(all_docs):
    ''' Allows the user to print out the contents of a particular document '''
    doc_num = int(input("Enter document number: "))
    print("Document #{}".format(doc_num))
    print(all_docs[doc_num])

def execute_actions(all_docs, word_dict):
    print()
    action = get_action()
    while action in {'1', '2'}:
        if action == '1':
            action_search_words(word_dict)
        elif action == '2':
            action_print_document(all_docs)
        action = get_action()
    else:
        print("Exiting program.")

# Main program starts here
document_file = input('Document collection: ')
all_docs = read_docs(document_file)
word_dict = build_dict(all_docs)
execute_actions(all_docs, word_dict)


        
    

