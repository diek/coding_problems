import numpy as np

my_array = np.array([[1, 2], [3, 4]])

print(np.sum(my_array, axis=0))      # Output : [4 6]
print(np.sum(my_array, axis=1))      # Output : [3 7]
print(np.sum(my_array, axis=None))   # Output : 10
print(np.sum(my_array))              # Output : 10

print(np.prod(my_array, axis=0))      # Output : [4 6]
print(np.prod(my_array, axis=1))      # Output : [3 7]
print(np.prod(my_array, axis=None))   # Output : 10
print(np.prod(my_array))              # Output : 10
