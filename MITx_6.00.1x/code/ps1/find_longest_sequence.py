# word = 'abcbcd'
# word = 'begghak'
# word = 'azcbobobegghakl'
# s = 'mairpkxdjxenvdwrl'
s = 'abcdefghijklmnopqrstuvwxyz'


longer_substring = ''
substring = ''
for letter in s:
    # first iteratiom
    if len(substring) < 1:
        substring = letter
    # letters are in sequence, add letter to substring
    elif substring[-1:] <= letter:
        substring = substring + letter
    # sequence is broken,
    else:
        # assign the longer string to longest, reset substring
        if len(substring) > len(longer_substring):
            longer_substring = substring
        substring = letter
# if all character are in order assign substring to longest
if len(longer_substring) < 1:
    longer_substring = substring

print 'Longest substring in alphabetical order is: ' + longer_substring
