import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Wrapper Executed')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def add(a, b, c=0):
    return a + b + c


print(add(2, 3, c=4))

# for i in range(10, 15, 1):
#     print(i, end=', ')

# var = "James" * 2  * 3
# print(var)

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add("Vicki")
# print(sampleSet)

# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)

# str = "pynative"
# print(str[1:3])

# var = "James Bond"
# print(var[2::-1])

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# for x in range(0.5, 5.5, 0.5):
#     print(x)

# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# x = 10
# y = 3
# print(x % y)

math_module = __import__('math')
print(math_module.sqrt(16))
