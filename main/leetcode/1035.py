class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        opt = [[[0, -1, -1] for i in range(len(B) + 1)] for j in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                # i - 1, j
                res1 = opt[i - 1][j][0]
                x1, y1 = opt[i - 1][j][1], opt[i - 1][j][2]
                for k in range(y1 + 1, j):
                    if B[k] == A[i - 1]:
                        res1 += 1
                        x1, y1 = i - 1, k
                        break

                # i, j - 1
                res2 = opt[i][j - 1][0]
                x2, y2 = opt[i][j - 1][1], opt[i][j - 1][2]
                for k in range(x2 + 1, i):
                    if A[k] == B[j - 1]:
                        res2 += 1
                        x2, y2 = k, j - 1
                        break

                if res1 >= res2:
                    opt[i][j][0], opt[i][j][1], opt[i][j][2] = res1, x1, y1
                else:
                    opt[i][j][0], opt[i][j][1], opt[i][j][2] = res2, x2, y2

        return opt[-1][-1][0]

