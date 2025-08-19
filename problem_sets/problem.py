# Small orange diamond
#  Input: "aaaabbbcca"
#  Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

# Write a function that converts the input to the output
def count_letter_sequence(a_string):
    ''' (string) -> list
    Return the character and count of consecutive character(s)

    >>> count_letter_sequence("aaaabbbcca")
    [('a', 4), ('b', 3), ('c', 2), ('a', 1)]
    >>> count_letter_sequence("aaaabbbccaa")
    [('a', 4), ('b', 3), ('c', 2), ('a', 2)]
    >>> count_letter_sequence("aaaabbbccaz")
    [('a', 4), ('b', 3), ('c', 2), ('a', 1), ('z', 1)]
    '''
    output = []
    tmp = []
    for idx, letter in enumerate(a_string):
        if idx + 1 < len(a_string):
            if a_string[idx + 1] == letter:
                tmp.append(letter)
            else:
                tmp.append(letter)
                output.append((tmp[0], len(tmp)))
                tmp = []
        else:
            if a_string[idx - 1] == letter:
                tmp.append(letter)
            else:
                tmp = []
                tmp.append(letter)
            output.append((tmp[0], len(tmp)))

    return output


strings = ["aaaabbbcca", "aaaabbbccaa", "aaaabbbccaz"]
for item in strings:
    print(count_letter_sequence(item))
