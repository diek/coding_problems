import random

# Define the number of elements in the list
n = 10
# Define the range for random numbers (inclusive)
min_val = 1
max_val = 30

# Generate the list
random_list = [random.randint(min_val, max_val) for _ in range(n)]
print(random_list)
