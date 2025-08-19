def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    In other words, myLog should return the largest power of b such
    that b to that power is still less than or equal to x.

    >>> myLog(16, 2)
    4
    >>> myLog(15, 3)
        2
    '''
    result = 0
    while b**(result+1) <= x:
        result += 1
    return result

print(myLog(16, 2))
print(myLog(15, 3))
print(myLog(625,5))
print(myLog(5764801, 7))

