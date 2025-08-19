# L4 PROBLEM 10
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = "aeiou"
    index = 0
    while index < len(vowels):
        if vowels[index] == char.lower():
            return True
        index = index + 1
    return False


print isVowel('A')
print isVowel('x')
print isVowel('b')
print isVowel('e')
print isVowel('u')
print isVowel('U')

