from collections import Counter

numbers = [0, 3, 3, 4, 5, 6, 4, 1, 2, 3, 4, 5, 49, 55, 76, 55]
count_dict = Counter(numbers)

print(dict(count_dict))

# numbers = [0, 3, 3, 4, 5, 6, 4, 1, 2, 3, 4, 5, 49, 55, 76, 55]

num_dict = {}

for num in numbers:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

for k, v in num_dict.items():
    print(k, v)
