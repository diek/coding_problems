def recurMultiply(a, b):
    if b == 1:
        return a
    else:
        return a + recurMultiply(a, b - 1)

print recurMultiply(5, 20)
print recurMultiply(4, 5)
