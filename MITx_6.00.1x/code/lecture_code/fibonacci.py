def fibonacci(x):
    '''assumes x is an int > 0
    returns Fibonacci of x'''
    # translates the assume into an assert, forcing the conditions. Return a boolean, if false stops program.
    assert type(x) == int and x > 0

    if x == 0 or x == 1:
        return 1
    else:
        # Every female alive at month n-2 will produce one female in month n;
        # These can be added those alive in month n-1 to get total alive in month n
        return fibonacci(x-1) + fibonacci(x-2)
