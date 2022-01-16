monthly_payment = 50.0
interest_rate_month1 = 1.5
interest_rate_month2 = 2.0
total_interest_paid = 0.0
month = 0

debt = float(input("Input the cost of the item in $: "))
if debt < 1000.0:
  interest_rate = interest_rate_month1
else:
  interest_rate = interest_rate_month2

while debt > 0:
  interest_paid = debt * interest_rate/100.0
  principal_payment = monthly_payment - interest_paid
  total_interest_paid += interest_paid

  if (debt >= monthly_payment):
    payment = monthly_payment
  else:
    payment = debt + interest_paid
  debt -= principal_payment
  if (debt < 0):
    debt = 0.0

  month += 1
  print("Month:", str(month), "Payment:", str(round(payment,2)), "Interest paid:", str(round(interest_paid, 2)), "Remaining debt:", str(round(debt, 2)))

print()
print("Number of months:", month)
print("Total interest paid:", str(round(total_interest_paid, 2)))