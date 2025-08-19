# Problem 1: Paying the Minimum
balance = 4213
annual_interest_rate = 0.2
monthly_payment_rate = 0.04

remaining_balance = balance
total_paid = 0

monthly_interest_rate = annual_interest_rate / 12.0
for m in range(1, 13):
    minimum_monthly_payment = monthly_payment_rate * remaining_balance
    total_paid = total_paid + minimum_monthly_payment
    unpaid_balance = remaining_balance - minimum_monthly_payment
    remaining_balance = (unpaid_balance) + (monthly_interest_rate * unpaid_balance)
    print(f"Month: {m}")
    print(f"Minimum monthly payment: {round(minimum_monthly_payment, 2)}")
    print(f"Remaining balance: {round(remaining_balance, 2)}")

print(f"Total paid: {round(total_paid, 2)}")
print(f"Remaining balance: {round(remaining_balance, 2)}")
pay_year = (total_paid + remaining_balance) / 12
print(f"minimum_monthly_payment to pay off in a year {round(pay_year)}")
