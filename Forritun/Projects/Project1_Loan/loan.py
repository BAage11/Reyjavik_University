loan_amount = float(input("Input the cost of the item in $: "))

months = 0
monthly_payment = float(50)
total_interest = 0 
sum_of_payments = 0
remaining_debt = loan_amount

while remaining_debt > 0:
  
    if loan_amount <= 1000:
        int_rate = 0.015 * remaining_debt
    else:
        int_rate = 0.02 * remaining_debt
  
    total_interest = total_interest + int_rate
    sum_of_payments = sum_of_payments + monthly_payment
    months += 1
    remaining_debt = (loan_amount - sum_of_payments) + total_interest

    if remaining_debt <= monthly_payment:
        break
    print("Month:", months, "Payment:", round(monthly_payment,2), "Interest paid:", round(int_rate,2), "Remaining debt:", round(remaining_debt,2))

if remaining_debt <= monthly_payment:
       print("Month:", months, "Payment:", round(monthly_payment,2), "Interest paid:", round(int_rate,2), "Remaining debt:", round(remaining_debt,2))

if remaining_debt >= 0:
    monthly_payment = remaining_debt
    months += 1

    if loan_amount <=1000:
        int_rate = 0.015 * remaining_debt
    else:
        int_rate = 0.02 * remaining_debt

    monthly_payment += int_rate
    remaining_debt += int_rate
    remaining_debt -= monthly_payment
    print("Month:", months, "Payment:", round(monthly_payment,2), "Interest paid:", round(int_rate,2), "Remaining debt:", round(remaining_debt,2))

total_interest = total_interest + int_rate

print ("                    ")
print("Number of months:", months)
print ("Total interest paid:", round(total_interest,2))
 