consonants = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z','W','Y', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y')
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
while True:
    englishWord_str = str(input("Enter a word: "))
    backup =englishWord_str
    if(englishWord_str == "."):
        quit()
    pigLatinWord = ""
    constans = ""
    yayoray = "yay"
    prin = False
    if(englishWord_str[0] in consonants):
        yayoray = "ay"

    for letter in englishWord_str:
        if(letter in consonants):
            constans += letter
            englishWord_str = englishWord_str[1:]
        else:
            print(englishWord_str + constans + yayoray)
            prin = True
            break
    if(prin == False):
        print(backup)