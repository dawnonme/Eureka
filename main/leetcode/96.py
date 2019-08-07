class Solution:
    def numTrees(self, n: int) -> int:
        if 0 <= n <= 1:
            return n

        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += (dp[i - j] * dp[j - 1])

        return dp[-1]
