def isPalindrome(s):
    # Internal procedures
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            # part one compare the first and last character, they must match
            # part two pulls out the remainder in between the first and last characters
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
