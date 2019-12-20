class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1, 10]
        for i in range(2, n + 1):
            cnt = 9
            for j in range(i - 1):
                cnt *= 9 - j
            dp.append(dp[i - 1] + cnt)
        return dp[n]
