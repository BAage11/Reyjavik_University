def shares_check(shares):
    try:
        shares = int(shares)
        return shares
    except ValueError:
        print('Invalid number!')
        return False

def price_check(price):
        dollars, numerator, denominator = price.split(" ")
        try:
            dollars = int(dollars)
            numerator = int(numerator)
            denominator = int(denominator)
            return (dollars, numerator, denominator)
        except ValueError:
            print('Invalid price!')
            return False

def loop(x):
    if x == "y":
        return True
    else:
        return False

def float_value(shares, dollars, numerator, denumerator):
    shares = int(shares)
    dollars = int(dollars)
    numerator = int(numerator)
    denumerator = int(denumerator)
    return (shares, dollars, numerator, denumerator)

keep_going = "y"
while loop(keep_going) == True:
    while loop(keep_going) == True:
        shares = input('Enter number of shares: ')
        if shares_check(shares) == False:
            continue
        else:
            break
    while loop(keep_going) == True:
        price = input('Enter price (dollars, numerator, denominator): ')
        if price_check(price) == False:
            continue
        else:
            dollars, numerator, denominator = price.split(" ")
            break
    
    share_price = ((float(shares) * float(dollars)) + (float(shares) * (float(numerator)/float(denominator))))
    print(share_price)
    keep_going = input('Wanna keep going? ')