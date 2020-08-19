class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = set(tuple(pt) for pt in mines)

        dp = [[[1] * 4 for j in range(N)] for i in range(N)]

        for (i, j) in mines:
            for k in range(4):
                dp[i][j][k] = 0

        for i in range(1, N):
            if (i, 0) not in mines:
                dp[i][0][0] = dp[i - 1][0][0] + 1

            if (0, i) not in mines:
                dp[0][i][1] = dp[0][i - 1][1] + 1

            if (N - 1 - i, N - 1) not in mines:
                dp[N - 1 - i][N - 1][2] = dp[N - i][N - 1][2] + 1

            if (N - 1, N - 1 - i) not in mines:
                dp[N - 1][N - 1 - i][3] = dp[N - 1][N - i][3] + 1

        for i in range(1, N):
            for j in range(1, N):
                if (i, j) not in mines:
                    dp[i][j][0] = dp[i - 1][j][0] + 1
                    dp[i][j][1] = dp[i][j - 1][1] + 1

                if (N - 1 - i, N - 1 - j) not in mines:
                    dp[N - 1 - i][N - 1 - j][2] = dp[N - i][N - 1 - j][2] + 1
                    dp[N - 1 - i][N - 1 - j][3] = dp[N - 1 - i][N - j][3] + 1

        ret = 0
        for i in range(N):
            for j in range(N):
                ret = max(ret, min(dp[i][j]))

        return ret
