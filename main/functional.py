'''
It's a memo for functional programming in Python.
'''

from random import random

# list comprehension
test = [random() for _ in range(1000)]

# map
test_times_2 = list(map(lambda x: 2 * x, test))

# filter
test_larger_than_1 = list(filter(lambda x: x > 1, test_times_2))

from functools import reduce  # Python library for functional programming

values = [1, 2, 3, 4]

# reduce
# 1 + 2 ==> 3, 3 + 3 ==> 6, 6 + 4 ==> 10
sum_values = reduce(lambda x, y: x + y, values)

# partial define (like curried function)
from functools import partial


def add(a, b):
    return a + b


add_two = partial(add, 2)
''' This function can be defined as:
def add_two(b):
    return 2 + b
'''

