word = input('Enter a word: ') 

vowels = 'aeuio'
yay=('yay') 
ay = ('ay')

while len(word) > 0 and word.isalpha(): 
# While loopa sem skilgreinir hvað orðið má vera til að þetta virki

    first_letter = word[0]
    if first_letter in vowels:
        print (word + yay) 
    
    elif first_letter not in vowels:
        for index, x in enumerate(word): 
        # For loopa sem skilar af sér sætistölunni á fyrsta sérhljóða
    
            if x in vowels: 
                first_vowel = word[index] 
                # Finn hvar fyrsti sérhljóðinn er og tekur index-ið hans (eins og rababari, þá er annar stafur sérhljóði og er því með index=1=a))
                consonants, rest =word.split(first_vowel) 
                print(first_vowel + rest + consonants + ay)
                break
       
            elif index == len(word) - 1: 
            # Ef lengdin á orðinu er jafnlangt og index þýðir það að orðið inniheldur ekki sérhljóða (gerði -1 út af því að index byrjar í 0)
                print(word + ay)   
    
    word = input('Enter a word: ')
    # Forritið biður aftur um input
