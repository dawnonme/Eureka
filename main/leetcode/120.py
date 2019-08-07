class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ''' Dynamic Programming
        '''
        dp = [[0] * len(l) for l in triangle]
        dp[0] = triangle[0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                l = dp[i - 1][j - 1] if j >= 1 else float('inf')
                m = dp[i - 1][j] if j < len(dp[i - 1]) else float('inf')
                ele = min(l, m)
                dp[i][j] = ele + triangle[i][j]
        return min(dp[-1])

    def minimum_total(self, triangle):
        ''' Linear Space
        '''
        dp = [triangle[0][0]]
        last = 0

        for i in range(1, len(triangle)):
            min_val = float('inf')
            min_last = last
            for j in [last, last + 1]:
                if min_val > triangle[i][j]:
                    min_val = triangle[i][j]
                    min_last = j
            dp.append(min_val + dp[i - 1])
            last = min_last
        return dp[-1]
