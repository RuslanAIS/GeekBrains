from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)

x = 0
for el in fact():
    if x >= 10:
        break
    else:
        print(el)
        x += 1
