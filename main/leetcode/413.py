class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        cnt, lo, hi = 0, 1, 2
        dp = [0] * len(A)
        diff = A[1] - A[0]
        while hi < len(A):
            if A[hi] - A[hi - 1] == diff:
                dp[hi] = dp[hi - 1] + (hi - lo)
            else:
                cnt += dp[hi - 1]
                diff = A[hi] - A[hi - 1]
                lo = hi
            hi += 1
        return cnt + dp[-1]
