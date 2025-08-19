def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    n = 1

    if aStr =="":
        return 0
    else:
        return n + lenRecur(aStr[n:])


print(lenRecur('derrick'))
print(lenRecur(""))
