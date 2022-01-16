
def error_check(number_of_shares):
 #""""Athugar hvort input sem slegið er inn af notanda, sé í raun tala. Ef ekki tala, þá prentast út villa og notandi beðinn um að slá inn aftur. """
  try:
    number_of_shares = int(number_of_shares)
    return number_of_shares
  except ValueError:
    print("Invalid number!")
    number_of_shares = input("Enter number of shares: ")

def error_check2(dollars, numerator, denominator):
 # """ Þegar notandi hefur slegið inn dollars-numerator-denominator, er innsláttur splittaður i lista sem inniheldur integers. Ef notandi hefur slegið eitthvað ranglega inn, annað en integers, prentast út villa og notandi beðinn um að reyna aftur. """
  global share_price
  while True:
    try:
      dollars = int(dollars)
      numerator = int(numerator)
      denominator = int(denominator)
      return True
    except ValueError:
      print("Invalid price!")
      share_price = input("Enter price (dollars, numerator, denominator): ")
    
# def int_to_float(a, b, c, d):
#   a = float(a)
#   b = float(b)
#   c = float(c)
#   d = float(d)


user_continue = "y"
while user_continue != "n":
  number_of_shares = input("Enter number of shares: ")
  error_check(number_of_shares)

  share_price = input("Enter price (dollars, numerator, denominator): ")
  dollars, numerator, denominator = share_price.split(" ")
  error_check2(dollars, numerator, denominator)
  dollars_float = float(dollars)
  numerator_float = float(numerator)
  denominator_float = float(denominator)
  number_of_shares_float = float(number_of_shares)

  market_price = ((dollars_float * number_of_shares_float) + ((numerator_float/denominator_float) * number_of_shares_float))
  print(number_of_shares, "shares with market price", dollars, numerator + "/" + denominator, "have value $", "{0:.2f}".format(market_price))
  user_continue = input("Continue: ")

