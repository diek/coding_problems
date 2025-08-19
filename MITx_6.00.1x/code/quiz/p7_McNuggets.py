def McNuggets(n):
    """
    n is an int
    6a + 9b + 20c = n
    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    return_value = False
    
    # The minimum amount is 6
    if (n < 6):
        return False;
    # The entered number matches an exact size McNuggets
    if ((n % 6 == 0)or(n % 9 == 0)or(n % 20 == 0)):
        return True
    # Use recursion to systematically reduce the number, starting at the highest number of 
    # nuggests
    if (return_value == False and n > 20):
        return_value = McNuggets(n - 20)

    if (return_value == False and n > 9):
        return_value = McNuggets(n - 9)

    if (return_value == False and n > 6):
        return_value = McNuggets(n - 6)

    return return_value

print(McNuggets(43))
print(McNuggets(33))
print(McNuggets(21))
print(McNuggets(6))
print(McNuggets(9))
print(McNuggets(0))


