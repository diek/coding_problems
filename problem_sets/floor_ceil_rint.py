import numpy as np

np.set_printoptions(legacy='1.13')

# floor of x is the largest int i where i =< x

# ceil - returns the ceiling of the input element-wise
# The ceiling of x is the smallest int i where i>= x

# rint - rounds to the nearest int of input element-wise


# Task
# You are given a 1-D array, A.
# print the floor,ceil and rint of all the elements of A

data = list(map(float, input().split()))

A = np.array(data)
print(A)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
