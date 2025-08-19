# 17 list comprehension problems in python
# [expression for item in iterable if condition]
# Create a list of squares of even numbers from 0 to 9
# https://www.tutorjoes.in/python_programming_tutorial/list_comprehensions_exercises_in_python#google_vignette
# count lines in a file
import math
import random

# Ex 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.
vowels = ["a", "e", "i", "o", "u"]
fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

fruits_two_vowels = [
    fruit for fruit in fruits if sum(1 for char in fruit if char.lower() in "aeiou") > 2
]
print(f"fruits two or more vowels: {fruits_two_vowels}\n")


def generate_random_numbers(count, min_val, max_val):
    """
    Generates a list of random integers within a specified range.

    Args:
        count (int): The number of random integers to generate.
        min_val (int): The minimum value for the random integers (inclusive).
        max_val (int): The maximum value for the random integers (inclusive).

    Returns:
        list: A list containing the generated random integers.
    """
    random_numbers = [random.randint(min_val, max_val) for _ in range(count)]
    return random_numbers


# Example usage:
# Generate 10 random numbers between -100 and 100
random_positive_negative = generate_random_numbers(50, -100, 100)

with open("sopranos_users.csv") as f:
    line_count = sum(1 for _ in f)

print(f"How many Sopranos Users: {line_count}\n")


even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares {even_squares}\n")

fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]
print(f"numbers_plus_one {numbers_plus_one}\n")
# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Ex 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

upper_fruit = [fruit.upper() for fruit in fruits]
print(f"upper_fruit {upper_fruit}\n")

# Ex 2 - create a variable named capitalized_fruits and use list comprehension
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalize_fruit = [fruit.capitalize() for fruit in fruits]
print(f"capitalize_fruit: {capitalize_fruit}\n")

# Ex 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.
vowels = ["a", "e", "i", "o", "u"]
fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

fruits_two_vowels = [
    fruit for fruit in fruits if sum(1 for char in fruit if char.lower() in "aeiou") > 2
]
print(f"fruits two or more vowels: {fruits_two_vowels}\n")

fruits_three_vowels = [
    fruit
    for fruit in fruits
    if sum(1 for char in fruit if char.lower() in "aeiou") == 3
]
# two_vowels = [letter in ]

# Ex 4 - make a variable named fruits_with_only_two_vowels.
# The result should be ['mango', 'kiwi', 'strawberry']
fruits_exact_two = [
    fruit
    for fruit in fruits
    if sum(1 for char in fruit if char.lower() in "aeiou") == 2
]

print(f"fruits exactly 2 vowels {fruits_exact_two}\n")

# Ex 5 - make a list that contains each fruit with more than 5 characters
fruit_five = [fruit for fruit in fruits if len(fruit) > 5]
print(f"fruit with more than 5 characters: {fruit_five}\n")

# Ex 6 - make a list that contains each fruit with exactly 5 characters
fruit_exact_five = [fruit for fruit in fruits if len(fruit) == 5]
print(f"fruit with exactly 5 characters: {fruit_exact_five}\n")

# Ex 7 - Make a list that contains fruits that have less than 5 characters
fruit_less_five = [fruit for fruit in fruits if len(fruit) < 5]
print(f"fruits that have less than 5 chars: {fruit_less_five}\n")

# Ex 8 - Make a list containing the number of characters in each fruit.
# Output would be [5, 4, 10, etc... ]
num_chars = [len(fruit) for fruit in fruits]
print(f"number of characters in each fruit {num_chars}\n")
# Ex 9 - Make a variable named fruits_with_letter_a that contains a list
# of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if ("a" in fruit)]
print(f"fruits that contain the letter 'a': {fruits_with_letter_a}\n")

# Ex 10 - Make a variable named even_numbers that holds only the even numbers
even_numbers = [number for number in range(20) if (number % 2 == 0)]
print(f"even numbers: {even_numbers}\n")

# Ex 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in range(20) if (number % 2 != 0)]
print(f"odd numbers: {odd_numbers}\n")

# Ex 12 - Make a variable named positive_numbers that holds only the
# positive numbers
positive_numbers = [number for number in random_positive_negative if number >= 0]
print(f"positive numbers: {positive_numbers}\n")

# Ex 13 - Make a variable named negative_numbers that holds only the
# negative numbers
negative_numbers = [number for number in random_positive_negative if number <= 0]
print(f"negative_numbers: {negative_numbers}\n")

# Ex 14 - use a list comprehension w/ a conditional in order to produce a
# list of numbers with 2 or more numerals
two_numerals = [
    number for number in random_positive_negative if len(str(abs(number))) > 1
]
print(f"two numerals or > : {two_numerals}\n")

# Ex 15 - Make a variable named numbers_squared that contains the numbers
# list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number**2 for number in range(10)]
print(f"numbers squared: {numbers_squared}\n")

# Ex 16 - Make a variable named odd_negative_numbers that contains only
# the numbers that are both odd and negative.
odd_negative_numbers = [
    number for number in random_positive_negative if (number % 2 != 0) and (number < 0)
]
print(f"Numbers that are both odd & negative: {odd_negative_numbers}\n")

# Ex 17 - Make a variable named numbers_plus_5. In it, return a list
# containing each number plus five.
num_list = [random.randint(1, 100) for _ in range(20)]
numbers_plus_5 = [number + 5 for number in num_list]
print(f"Number plus five: {numbers_plus_5}")

# BONUS Make a variable named "primes" that is a list containing the prime
# numbers in the numbers list. *Hint* you may want to make or find a helper
# function that determines if a given number is prime or not.


def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of n
    # We only need to check up to the square root because if a number has a divisor
    # greater than its square root, it must also have a divisor smaller than its square root.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (
                False  # If n is divisible by any number in this range, it's not prime
            )

    return True


primes = [number for number in num_list if is_prime(number)]
print(f"Primes: {primes}")
