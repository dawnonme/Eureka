class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length = 1000
        max_length = 2 * length + 1
        if S > length or S < -length:
            return 0
        dp = [[0] * max_length for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                dp[i][num + length] += 1
                dp[i][-num + length] += 1
            else:
                for j in range(max_length):
                    if dp[i - 1][j] != 0:
                        dp[i][j + num] += dp[i - 1][j]
                        dp[i][j - num] += dp[i - 1][j]
        return dp[-1][S + length]
