loan_amount = float(input("Enter the loan amount: "))

months = 0
montly_payment = 50
total_interest = 0

sum_of_payments = 0
remaining_debt = loan_amount

while remaining_debt > 0:   
  if loan_amount <= 1000:
    int_rate = 0.015 * remaining_debt
  else:
    int_rate = 0.02 * remaining_debt

  total_interest += int_rate
  sum_of_payments += montly_payment
  months += 1
  remaining_debt = (loan_amount - sum_of_payments) + total_interest
  
  print("Months:", months, "Payment:", montly_payment, "Interest paid:", round(int_rate, 2), "Remaining debt:", round(remaining_debt, 2))

print("Number of months:", months, "Total interest paid:", round(total_interest, 2))
