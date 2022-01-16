
def error_check(number_of_shares):
  """"Athugar hvort input sem slegið er inn af notanda, sé í raun tala. Ef ekki tala, þá prentast út villa og notandi beðinn um að slá inn aftur. """
  try:
    number_of_shares = int(number_of_shares)
    return number_of_shares
  except ValueError:
    print("Invalid number!")
    number_of_shares = input("Enter number of shares: ")

def error_check2(dollars, numerator, denominator):
  """ Þegar notandi hefur slegið inn dollars-numerator-denominator, er innsláttur splittaður i lista sem inniheldur integers. Ef notandi hefur slegið eitthvað ranglega inn, annað en integers, prentast út villa og notandi beðinn um að reyna aftur. """
  global share_price
  while True:
    try:
      dollars = int(dollars)
      numerator = int(numerator)
      denominator = int(denominator)
      return True
    except ValueError:
      print("Invalid price!")
      share_price = input("Enter price (dollars, numerator, denominator):")
    
number_of_shares = input("Enter number of shares: ")
error_check(number_of_shares)

share_price = input("Enter price (dollars, numerator, denominator):")
# Skipta input frá notanda milli bila (" ") og búa til breytur út frá því.
share_price = (share_price.split(" "))
dollars = share_price[0]
numerator = share_price[1]
denominator = share_price[2]
error_check2(dollars, numerator, denominator)

# Breyta string í float
dollars_float = float(dollars)
numerator_float = float(numerator)
denominator_float = float(denominator)
number_of_shares_float = float(number_of_shares)

market_price = ((dollars_float + (numerator_float / denominator_float)) * number_of_shares_float)

print(number_of_shares, "shares with market price", dollars, numerator + "/" + denominator, "have value $", "{0:.2f}".format(market_price))

user_continue = input("Continue: ")
if user_continue == "y":
  number_of_shares = input("Enter number of shares: ")
  error_check(number_of_shares)


