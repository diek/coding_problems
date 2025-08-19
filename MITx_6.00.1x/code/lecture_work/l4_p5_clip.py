def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''

    # Your code here
    # return max(min(lo, x),min(x,hi))
    # return min(max(x, lo), hi)
    return max(max(lo, x),min(x,hi))
    # return min(x, hi)

    # - lo, when x < lo and x < hi -> 9 is not less than 4, 9 is not less than 7 -> NO
    # - hi, when x > lo and x > hi -> 9 is greater than 4, 9 is greater than 7 -> YES
    # - x, otherwise - NO

print clip(4,9,7) # Should rtn 7

    # - lo, when x < lo and x < hi -> 12 is not less than 8 , 12 is less than 13 -> NO
    # - hi, when x > lo and x > hi -> 12 is greater than 8, 9 is not greater 13 -> NO
    # - x, otherwise - YES

print clip(8,12,13) # Should rtn 12

    # - lo, when x < lo and x < hi -> 12 < 8 , 12 < 13 ->
    # - hi, when x > lo and x > hi -> 12 > 8, 9 i> 13 ->
    # - x, otherwise ->

print clip(-3.62, -9.13, 5.79) # Should rtn -3.62, fails


print clip(-1.79, -3.9, 2.93) # Should rtn -1.79, fails
