class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0, 0, 2, 3]

        for i in range(4, n + 1):
            dp.append(max(dp[i - 2] * 2, dp[i - 3] * 3))
        return dp[-1]

    def pure_dp_without23(self, n):
        dp = [0, 0, 1]
        for i in range(3, n + 1):
            lo = 1
            hi = i - 1
            max_prod = 0
            while lo <= hi:
                max_prod = max(max_prod, max(hi, dp[hi]) * max(lo, dp[lo]))
                lo += 1
                hi -= 1
            dp.append(max_prod)
        return dp[-1]
