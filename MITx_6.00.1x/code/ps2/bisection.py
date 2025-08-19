# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 29157.09

# Test Case 2:
balance = 999999
annualInterestRate = 0.18

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 90325.03

monthlyInterestRate = annualInterestRate / 12
lower_bound = balance / 12
upper_bound = (balance * (1 + monthlyInterestRate) ** 12) / 12
originalBalance = balance
lowestBalance = 0.01

while abs(balance) > lowestBalance:
    # Restart check
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = ((upper_bound - lower_bound) / 2) + lower_bound

    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    if balance > 0:
        # balance is over, need higher payment -> increase lower bound
        lower_bound = payment
    else:
        # balance is under, we need a lower payment -> decrease upper bound
        upper_bound = payment

# When the while loop terminates, we know we have our answer!
print "Lowest Payment:", round(payment, 2)
