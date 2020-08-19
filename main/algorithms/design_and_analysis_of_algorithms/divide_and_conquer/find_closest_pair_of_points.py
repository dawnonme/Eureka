"""
In this problem, distance means Euclidean Distance. Moreover, for sake of
simplicity, all the points are in 2-D plane.

Task is to find the smallest distance between any pair of points in a point
set.

Naive algorithm: O(n^2)
Divide and conquer: O(nlogn) 

"""


class Point:
    def __init__(self, attr=[]):
        self.attr = attr
        self.dim = len(attr)

    def euclidean_distance(self, pt):
        from math import sqrt

        if pt.dim != self.dim:
            raise ValueError("Dimensions mismatch!")
        dis = 0.0
        for i in range(self.dim):
            dis += (self[i] - pt[i])**2
        return sqrt(dis)

    def __getitem__(self, idx):
        return self.attr[idx]


def find_closest_pair_of_points_naive(pt_set):
    min_dis = float('inf')
    # pt_pair = None
    for i in range(len(pt_set) - 1):
        for j in range(i + 1, len(pt_set)):
            dis = pt_set[i].euclidean_distance(pt_set[j])
            if dis < min_dis:
                min_dis = dis
                # pt_pair = (i, j)
    return min_dis


def find_closest_pair_of_points_recursive(pt_set):
    if not pt_set or len(pt_set) < 2:
        raise ValueError('Invalid input!')
    pt_set.sort(key=lambda x: x[0])
    return _find_closest_pair_of_points_recursive(pt_set)


def _find_closest_pair_of_points_recursive(pt_set):
    if len(pt_set) == 1:
        return float('inf')
    if len(pt_set) == 2:
        return pt_set[0].euclidean_distance(pt_set[1])
    left_set = pt_set[:len(pt_set) // 2]
    right_set = pt_set[len(pt_set) // 2:]

    left_dis = _find_closest_pair_of_points_recursive(left_set)
    right_dis = _find_closest_pair_of_points_recursive(right_set)

    dis = min(left_dis, right_dis)

    pivot = len(pt_set) // 2
    pivot_x = (pt_set[pivot][0] + pt_set[pivot - 1][0]) / 2

    lo = pivot - 1
    hi = pivot

    while lo > 0 and pivot_x - pt_set[lo][0] <= dis:
        lo -= 1

    while hi < len(pt_set) - 1 and pt_set[hi][0] - pivot_x <= dis:
        hi += 1

    left_gap = pt_set[lo: pivot]
    right_gap = pt_set[pivot: hi + 1]

    left_gap.sort(lambda x: x[1])
    right_gap.sort(lambda x: x[1])


if __name__ == '__main__':
    from random import randint

    for i in range(10):
        num_pts = randint(20, 100)
        pt_set = []
        for j in num_pts:
            pt_x, pt_y = randint(-100, 100), randint(-100, 100)
            pt_set.append(Point([pt_x, pt_y]))

        real_dis = find_closest_pair_of_points_naive(pt_set)
        test_dis = find_closest_pair_of_points_recursive(pt_set)

        if real_dis != test_dis:
            print("Test case: %d failed! Expect: %f, get: %f." %
                  (i, real_dis, test_dis))
        else:
            print("Test case: %d succeeded! Result: %f." % (i, test_dis))
