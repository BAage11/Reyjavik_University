# https://www.sololearn.com/Discuss/193056/write-a-python-program-which-will-ask-user-to-enter-3-numbers-your-program-will-output-the-sum-and

user_shares = input("Enter number of shares: ")
user_price = input("Enter price (dollars, numerator, denominator: ")

def price_check(user_shares, user_price):
  try:
    user_price2 = (float, user_price.split(" "))    # integer - String - checka svo integer
    market_price = float(user_shares*(user_price2[0]*(user_price2[1]/user_price2[2])))
    
    print(user_shares, "shares with market price", user_price2, "have value $", market_price)
    
    user_continue = input("Continue: ")
    if user_continue == "y":
      return True
    elif user_continue == "n":
      return False

  except:
    print("Invalid price!")
    user_price = input("Enter price (dollars, numerator, denominator: ")


price_check(user_shares, user_price)
