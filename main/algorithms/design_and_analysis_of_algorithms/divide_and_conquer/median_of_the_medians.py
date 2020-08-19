""" 
In this problem, median is defind below:
the median of a set S of n integers = the ceil(n / 2)-th smallest element in S

Task is to find the median in any arrays.

Naive algorithm: O(nlogn)
Median of the medians algorithm: O(n)
"""

from math import ceil


def select(arr, k):
    if not arr or k < 0 or k >= len(arr):
        raise ValueError('Invalid input!')
    return _select(arr, k)


def _select(arr, k):
    # base case
    if len(arr) <= 5:
        arr.sort()
        return arr[k]

    # divide array into sunarrays with 5 elements each
    num_groups = len(arr) // 5
    groups = []
    for i in range(num_groups):
        groups.append(arr[i * 5:(i + 1) * 5])
    if num_groups * 5 < len(arr):
        groups.append(arr[num_groups * 5:])

    # find median for each group
    medians = [_select(group, ceil(len(group) / 2) - 1) for group in groups]

    # take the median of the medians as pivot
    pivot = _select(medians, ceil(len(medians) / 2) - 1)

    # partition the original array
    lower, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            lower.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    if k >= len(lower) and k < len(lower) + len(equal):
        return pivot
    elif k < len(lower):
        return _select(lower, k)
    return _select(larger, k - len(lower) - len(equal))


def median_of_the_medians(arr):
    return select(arr, ceil(len(arr) / 2) - 1)


def naive_median(arr):
    if len(arr) % 2 == 1:
        return sorted(arr)[len(arr) // 2]
    return sorted(arr)[len(arr) // 2 - 1]


if __name__ == '__main__':
    from random import randint

    for i in range(10):
        arr = [randint(-1000, 1000) for _ in range(randint(20, 200))]

        median_test = median_of_the_medians(arr)

        median_real = naive_median(arr)

        if median_test != median_real:
            print("Test case: %d failed! Expect: %f, get: %f." %
                  (i, median_real, median_test))
        else:
            print("Test case: %d succeeded! Result: %f." % (i, median_test))
