#https://github.com/bjorksigur/Skilaverkefni-4.git

def error_check(shares): 
    var1 = True
    while var1 == True:
        shares = input("Enter number of shares: ") 
        try: 
            shares = int(shares)
            if shares == int: 
                var1 = False
            return(shares)
        except ValueError:
            print("Invalid number!") 
            

def error_check_price(dollars, n, d):
    var1 = True
    while var1 == True:
        dollars, n, d = input("Enter price (dollars, numerator, denominator): ").split()
        try:
            dollars = int(dollars)
            n = int(n)
            d = int(d)
            if dollars == int and n == int and d == int:
                var1 = False
            return(dollars, n, d)
        except ValueError:
            print("Invalid price!")
        

def value_price_format(value_price):
    return ("${:.2f}".format(value_price))

shares = 1
dollars = 0
n = 0
d = 0

while shares > 0: 
    shares = error_check(shares)
    dollars, n, d = error_check_price(dollars, n, d)
    fraction = n / d
    whole_price = (fraction + dollars)
    value_price = (whole_price * shares)
    
    print(shares,"shares with market price",dollars,"{}/{}".format(n,d),"have value",value_price_format(value_price))
    
    Continue = input("Continue: ")
    if Continue != "y":
        break 

     