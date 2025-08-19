def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1

    result = base
    while exp > 1:
        result = result * base
        exp -= 1
    return result

print iterPower(5.31, 0)
print iterPower(4.54, 5)
