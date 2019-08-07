class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        if len(x) < len(y):
            diff = len(y) - len(x)
            x = '0' * diff + x
        elif len(x) > len(y):
            diff = len(x) - len(y)
            y = '0' * diff + y
        dis = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                dis += 1
        return dis

    def hamming_distance(self, x, y):
        n = x ^ y
        dis = 0

        while n > 0:
            dis += n & 1
            n >>= 1
        return dis
