loan_amount = float(input("Input the cost of the item in $: "))

month = 0
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
  month += 1
  remaining_debt = (loan_amount - sum_of_payments) + total_interest
  
  if remaining_debt <= 0:
    remaining_debt = (montly_payment * month
  ) - sum_of_payments
    print("Month:", month, "Payment:", montly_payment, "Interest paid:", round(int_rate, 2), "Remaining debt:", round(remaining_debt, 2))
    break
  
  print("Month:", month, "Payment:", montly_payment, "Interest paid:", round(int_rate, 2), "Remaining debt:", round(remaining_debt, 2))

print("Number of month:", month, "Total interest paid:", round(total_interest, 2))
