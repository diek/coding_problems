numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
result = []
for number in numbers:
    if number % 2 == 0:
        result.append(number)
print(result)

result = [number for number in numbers if number % 2 == 0]
print(result)

#  {x^2: x is a natural number less than 10 }
vowels = ['a', 'e', 'i', 'o', 'u']
sentence = "I am working on this excercise were I have to count the vowels for every string in a list."
x = []
c_result = [letter for letter in sentence if letter in vowels]
print(c_result)
