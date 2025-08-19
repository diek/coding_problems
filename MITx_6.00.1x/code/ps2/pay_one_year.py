# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310


# Test Case 2:
# balance = 4773
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 440

# Test Case 3:
balance = 3926
annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 360

def find_lowest(balance_in, monthy_interest_rate):
    min_monthly_payment = 10
    for x in range(1, 200):
        balance = balance_in

        for month in range(1, 13):
            balance = (balance - min_monthly_payment) + (monthy_interest_rate * (balance - min_monthly_payment))

        if balance < 0:
            return min_monthly_payment

        else:
            min_monthly_payment = min_monthly_payment + 10


monthy_interest_rate = annualInterestRate/12.0
lowest_payment = find_lowest(balance, monthy_interest_rate)
print('Lowest Payment: ' + str(round(lowest_payment,2)))


# Hint: A way of structuring your code
# If you are struggling with how to structure your code, think about the following:
# Given an initial balance, what code would compute the balance at the end of the year?

# Now imagine that we try our initial balance with a monthly payment of $10. If there
# is a balance remaining at the end of the year, how could we write code that would reset
# the balance to the initial balance, increase the payment by $10, and try again (using
# the same code!) to compute the balance at the end of the year, to see if this new payment value is large enough.

# I'm still confused!
# A good way to implement this problem will be to use a loop structure. You may want to refresh your understanding of while loops. Think hard about how the program will know when it has found a good minimum monthly payment value - when a good value is found, the loop can terminate.
# Be careful - you don't want to overwrite the original value of balance. You'll need to save that value somehow for later reference!
