def fact_iterate(n):
    ''' assumes that n is an int > 0
    returns n!, note that ! is said as bang'''


    res = 1

    while n > 1:
        res = res * n
        n -= 1
    return res

def fact_recursive(n):
    ''' assumes that n is an int > 0
    returns n!'''


    if n == 1:
        return n
    return n*fact_recursive(n-1)


print fact_iterate(7)
print fact_recursive(7)
