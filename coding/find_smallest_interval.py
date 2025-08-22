import sys
import math

# from contextlib import redirect_stdout


def find_smallest_interval(nums):
    smallest = []
    for num in nums:
        for idx, num2 in enumerate(nums):
            try:
                diff = nums[idx + 1] - num
                if diff != 0:
                    smallest.append(abs(diff))

            except IndexError:
                continue

    return min(smallest)


print(find_smallest_interval([1, 6, 4, 8, 2]))
