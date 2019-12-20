class Solution:
    def divisorGame(self, N: int) -> bool:
        from math import sqrt
        if N == 1 or N == 3:
            return False
        if N == 2:
            return True
        dp = [False] * (N + 1)
        dp[2] = True

        for i in range(4, N + 1):
            factor = int(sqrt(i))
            dp[i] = any(not dp[i - j]
                        for j in range(1, factor + 1) if i % j == 0)
        return dp[-1]
