def get_shares():
    ''' Returns a valid number of shares input by user '''    
    while True:
        try:
            shares = input("Enter number of shares: ")
            return int(shares)
        except ValueError:
            print("Invalid number!")

def get_price_info_as_strings():
    ''' Returns price info input by user as strings '''
    price_info = input("Enter price (dollars, numerator, denominator): ")
    return price_info.split()
    
def get_price_info():
    ''' Returns valid price info input by user '''
    while True:
        try:
            dollars, numerator, denominator = get_price_info_as_strings()
            return int(dollars), int(numerator), int(denominator)
        except ValueError:
            print("Invalid price!")    

def convert(dollars, numerator, denominator):
    ''' Converts a price stated with integer values into a float '''
    return dollars + numerator/denominator

def displayResult(shares, dollars, numerator, denominator, value):
    ''' Display results '''
    print("{:d} shares with market price {:d} {:d}/{:d} have value ${:.2f}".format(shares, dollars, numerator, denominator, value))

# Main program starts here
repeat = 'y'
while repeat.lower() == 'y':
    # Read data from user and compute and display stock value
    shares = get_shares()
    dollars, numer, denom = get_price_info()
    price = convert(dollars, numer, denom)
    value = price * shares
    displayResult(shares, dollars, numer, denom, value)
    repeat = input("Continue: ")