# Global scope


# def outer_func():
#     # Non-local scope
#     def inner_func():
#         # Local scope
#         print(some_variable)

#     inner_func()


# some_variable = "Hello from global scope!"
# outer_func()


a = 10
b = 20
c = 30


def print_globals():
    print(a, b, globals()["c"])
    c = 100
    print(c)


print_globals()
# counter = 0


# def increment():
#     global counter
#     counter += 1


# increment()
# print(counter)
# # 1
# increment()
# print(counter)
# 2
def set_global_variable():
    global number
    number = 7


set_global_variable()
print(number)


def dynamic_global_variable(name, value):
    globals()[name] = value


dynamic_global_variable("number", 42)
print(number)
