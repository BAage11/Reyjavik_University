shares = ""
market_value = ""

def contain_shares(shares, type):
  try:
    shares = input(shares)
    if shares == int:
      return True
  except Exception:
    print("Invalid price!")

def contain_price(dollars, numerator, denominator):
  try:
    if dollars and numerator and denominator == int:
      market_value = shares*(dollars*(numerator/denominator))
      print(shares, "shares with market price", dollars, numerator+"/"+denominator, "have value $", market_value)
  except Exception:
    print("Invalid price!") 


print(contain_shares("Enter number of shares: ", int))
print(contain_price("Enter price (dollars, numerator, denominator): "))

