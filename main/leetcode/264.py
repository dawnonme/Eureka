class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2 = p3 = p5 = 0
        next_2, next_3, next_5 = 2, 3, 5

        for _ in range(1, n):
            add = min(next_2, next_3, next_5)
            dp.append(add)
            if add == next_2:
                p2 += 1
                next_2 = dp[p2] * 2
            if add == next_3:
                p3 += 1
                next_3 = dp[p3] * 3
            if add == next_5:
                p5 += 1
                next_5 = dp[p5] * 5
        return dp[-1]
