class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col, ans = len(matrix), len(matrix[0]), 0
        dp = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    left = dp[i - 1][j] if i > 0 else 0
                    up = dp[i][j - 1] if j > 0 else 0
                    prev = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = min([left, up, prev]) + 1
                    ans = max(ans, dp[i][j])

        return ans**2
