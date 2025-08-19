import numpy as np

nums = list(map(int, input().split()))
n, m = nums
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.array(a/b, int))
print(np.mod(a, b))
print(np.power(a, b))

data_a = input().split()
data_b = input().split()

a = np.array([int(num) for num in data_a if num.isdigit()])
b = np.array([int(num) for num in data_b if num.isdigit()])

print(np.inner(a, b))
print(np.outer(a, b))
30 may - 02 Jun
