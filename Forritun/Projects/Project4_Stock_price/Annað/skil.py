def shares_check(shares):
    """ Athugar hvort að notandi hafi skrifað inn integer sem input. Ef ekki, þá skilar kóðinn villu. """
    try:
        shares = int(shares)
        return shares
    except ValueError:
        print('Invalid number!')
        return False

def price_check(price):
    """ Skipting input niður í þrjár breytur og tjékkar hvort þær innihalda innslegnar tölur. Ef ekki, prentast út villa til að láta notanda vita að ranglega hafi verið slegið inn. """
    dollars, numerator, denominator = price.split(" ")
    try:
        dollars = int(dollars)
        numerator = int(numerator)
        denominator = int(denominator)
        return (dollars, numerator, denominator)
    except ValueError:
        print('Invalid price!')
        return False

# Prentar út markaðsvirði hlutabréfa, miðað við innslegnar upplýsingar notanda. Athugar svo einnig hvort að notandi vilji halda áfram, þ.e. að fá markaðsvirði annarra bréfa.
keep_going = "y"
while keep_going == "y":
    while True:
        shares = input('Enter number of shares: ')
        if shares_check(shares) == False: 
            continue
        else:
            break
    while True:
        price = input('Enter price (dollars, numerator, denominator): ')
        if price_check(price) == False:
            continue
        else:
            dollars, numerator, denominator = price.split(" ")
            break
    
    share_price = ((float(shares) * float(dollars)) + (float(shares) * (float(numerator)/float(denominator))))

    print(shares,'shares with market price', dollars, numerator+'/'+denominator,'have value $'+"{0:.2f}".format(share_price))
    keep_going = input('Continue: ')
