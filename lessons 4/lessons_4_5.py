from functools import reduce


def my_func(x, y):
    return x * y


print(y for y in range(100, 1001) if y % 2 == 0)
print(reduce(my_func,[y for y in range(100, 1001) if y % 2 == 0]))
