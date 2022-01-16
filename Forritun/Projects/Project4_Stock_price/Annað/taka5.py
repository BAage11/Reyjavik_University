number_of_shares = input("Enter number of shares: ")
share_price = input("Enter price (dollars, numerator, denominator) :")

def error_check(number_of_shares):
  """"Athugar hvort input sem slegið er inn af notanda, sé í raun tala. Ef ekki tala, þá prentast út villa og notandi beðinn um að slá inn aftur. """
  try:
    number_of_shares = int(number_of_shares)
#    share_price = list(map(int, share_price))
    return number_of_shares
  except ValueError:
    print("Invalid number!")
    number_of_shares = input("Enter number of shares: ")

def error_check2(share_price):
  """ Þegar notandi hefur slegið inn dollars-numerator-denominator, er innsláttur splittaður i lista sem inniheldur integers. Ef notandi hefur slegið eitthvað ranglega inn, annað en integers, prentast út villa og notandi beðinn um að reyna aftur. """
  try:
    share_price = (share_price.split(" "))
#    share_price = list(map(int, share_price))
    return share_price
  except ValueError:
    print("Invalid price!")
    share_price = input("Enter price (dollars, numerator, denominator) :")


error_check(number_of_shares)
error_check2(share_price)

share_price_float = float(share_price)
print(share_price_float, type(share_price))    # athuga hvað prentast út


# market_price = ((share_price[0] + (share_price[1] / share_price[2])) * number_of_shares)
# print(number_of_shares, "shares with market price ", share_price, "have value $", float(market_price,2)

#user_continue = input("Continue: ")
#if user_continue == "y":
#  number_of_shares = input("Enter number of shares: ")
#  share_price = input("Enter price (dollars, numerator, denominator) :")
#