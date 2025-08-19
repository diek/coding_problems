# import numpy as np

# # a, b, c = map(int, input().split())
# # arrA = np.array([input().split() for _ in range(a)], int)
# # arrB = np.array([input().split() for _ in range(b)], int)
# # print(np.concatenate((arrA, arrB), axis=0))

# # nums = list(map(int, input().split()))
# # print(np.zeros(nums, dtype=int))
# # print(np.ones(nums, dtype=int))

# print(str(np.eye(*map(int, input().split()))).replace('1', ' 1').replace('0', ' 0'))
import numpy

numpy.set_printoptions(legacy='1.13')


nums = list(map(int, input().split()))
n, m = nums
print(f"Type: {type(n)}")

print(numpy.eye(n, m))
