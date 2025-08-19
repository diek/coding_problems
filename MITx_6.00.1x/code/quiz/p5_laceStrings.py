def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Make strings equal, strip any remaining char if one string longer
    # This will ensure that iterating over each string will be equal
    if len(s1) > len(s2):
        (s1, tail) = (s1[0:len(s2)], s1[len(s2):])
    elif len(s1) < len(s2):
        (s2, tail) = (s2[0:len(s1)], s2[len(s1):])
    else:
        tail = ""

    # create a new container
    laced_up = []
    for i in range(len(s1)):
        laced_up.append(s1[i])
        laced_up.append(s2[i])
    return "".join(laced_up) + tail



result = laceStrings('abcd','efghi')
if result == 'aebfcgdhi':
    print 'success'
