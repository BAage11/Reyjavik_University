user_shares = input("Enter number of shares: ")
user_price = input("Enter price (dollars, numerator, denominator): ")

def price_check(user_shares, user_price):
  try:
    user_price2 = (user_price.split(" "))    
    if user_shares == int:
      return True
    if user_price2 == int or float:
      return True      
  except ValueError:
    print("Invalid price!")
    user_price = input("Enter price (dollars, numerator, denominator: ")    

price_check(user_shares, user_price)

if user_price2 == int and user_shares == int:
  market_price = float(user_shares*(user_price2[0]*(user_price2[1]/user_price2[2])), 2)
  print(user_shares, "shares with market price", user_price2, "have value $", et_price)

if user_price2 == float and user_shares == int:
  market_price = float(user_shares*(user_price2[0]*(user_price2[1]/user_price2[2])), 2)
  print(user_shares, "shares with market price", user_price2, "have value $", et_price)

user_continue = input("Continue: ")
if user_continue == "y":
  user_shares = input("Enter number of shares: ")
  user_price = input("Enter price (dollars, numerator, denominator): ")
elif user_continue == "n":
  user_shares = input("Enter number of shares: ")
  user_price = input("Enter price (dollars, numerator, denominator): ")
