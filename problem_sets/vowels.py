#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def count_vowels(substring):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for letter in substring:
        if letter in vowels:
            count += 1
    return count


def findSubstring(s, k):
    # Write your code here
    stop = k
    highest_count = 0
    most_vowels = ""
    for idx, _ in enumerate(s):
        sub = s[idx:stop]
        vowels = count_vowels(sub)
        if highest_count < vowels:
            highest_count = vowels
            most_vowels = sub
        stop += 1

    return most_vowels


def main():
    print(findSubstring("eiuaooo", 4))


if __name__ == "__main__":
    main()
