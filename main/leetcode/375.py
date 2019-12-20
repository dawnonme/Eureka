class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] means the minimal cost to guess the number in range [i, j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # find dp[lo][hi]
        def helper(lo, hi):
            if lo >= hi:
                return 0

            if dp[lo][hi] != 0:
                return dp[lo][hi]

            res = float('inf')
            for i in range(lo, hi + 1):
                # your number is i, you will either pick number less than i or number more than
                # i, to make sure you will be able to guess out, you will beed to pay more
                tmp = i + max(helper(lo, i - 1), helper(i + 1, hi))

                # but meanwhile, minimize the cost
                res = min(res, tmp)
            dp[lo][hi] = res
            return res

        return helper(1, n)
