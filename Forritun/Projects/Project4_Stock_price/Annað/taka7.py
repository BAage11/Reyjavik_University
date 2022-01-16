
number_of_shares = input("Enter number of shares: ")
share_price = input("Enter price (dollars, numerator, denominator) :")

# Splitta input frá notanda milli bila (" ") og búa til breytur út frá því.
share_price = (share_price.split(" "))
dollars = share_price[0]
numerator = share_price[1]
denominator = share_price[2]

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
      share_price = input("Enter price (dollars, numerator, denominator) :")


error_check(number_of_shares)
error_check2(dollars, numerator, denominator)

dollars_int = int(dollars)
numerator_int = int(numerator)
denominator_int = int(denominator)
number_of_shares_int = int(number_of_shares)

market_price = ((dollars_int + (numerator_int / denominator_int)) * number_of_shares_int)

print(number_of_shares_int, "shares with market price ", dollars_int, numerator_int,"/",denominator_int, "have value $", float(market_price,2)