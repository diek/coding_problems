# the key thing to think about is "What does a balance greater/lower than zero mean?" Well, if the balance
# is greater than 0 at the end of 12 months, your payments failed to pay off the total debt: so they are too small.
# If the balance is below zero then you've paid too much: in this case, your payments are too large

# You are on the right track: though you'll need a more advanced way to figure out the end balance for a given payment.
# Remember that for a given payment, you will do the following for each of 12 months:
# 1) Have an initial Balance
# 2) Subtract your payment
# 3) Add interest on the current balance
# To do this, I used a function call which gave parameters for current balance/payment/interest rate and returned the
# year-end balance.

# Test Case 1:
# balance = 320000
# annual_interest_rate = 0.2

balance = 24
annual_interest_rate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 29157.09

# Test Case 2:
# balance = 999999
# annual_interest_rate = 0.18

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 90325.03


def pay_one_year(annual_interest_rate, balance):
    lower_bound = balance / 12
    upper_bound = (balance * (1 + monthly_interest_rate) ** 12) / 12
    starting_balance = balance
    lowest_balance = 0.01

    while abs(balance) > lowest_balance:
        # Start/Reset check
        balance = starting_balance
        # Calculate a new monthly payment value from the bounds
        payment = ((upper_bound - lower_bound) / 2) + lower_bound

        # Can payment pay off balance in 12 months
        for month in range(12):
            balance -= payment
            balance *= 1 + monthly_interest_rate
            print(round(balance, 2))

        if balance > 0:
            # balance is over, need higher payment -> increase lower bound
            lower_bound = payment
        else:
            # balance is under, we need a lower payment -> decrease upper bound
            upper_bound = payment

    return payment


monthly_interest_rate = annual_interest_rate / 12

print(f"Lowest Payment: {round(pay_one_year(monthly_interest_rate, balance), 2)}")
